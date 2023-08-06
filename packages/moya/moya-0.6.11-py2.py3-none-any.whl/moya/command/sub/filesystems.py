from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os

from ...command import SubCommand
from ...wsgi import WSGIApplication
from ...console import Cell
from ...compat import text_type, raw_input

from fs.opener import fsopendir
from fs.errors import FSError
from fs.multifs import MultiFS
from fs.mountfs import MountFS
from fs.path import dirname


def _ls(console, file_paths, dir_paths, format_long=False):
    """Cannibalized from pyfileystem"""

    dirs = frozenset(dir_paths)
    paths = sorted(file_paths + dir_paths, key=lambda p: p.lower())

    def columnize(paths, num_columns):
        col_height = (len(paths) + num_columns - 1) / num_columns
        columns = [[] for _ in range(num_columns)]
        col_no = 0
        col_pos = 0
        for path in paths:
            columns[col_no].append(path)
            col_pos += 1
            if col_pos >= col_height:
                col_no += 1
                col_pos = 0

        padded_columns = []

        def wrap(path):
            return (path in dirs, path.ljust(max_width))

        for column in columns:
            if column:
                max_width = max([len(path) for path in column])
            else:
                max_width = 1
            max_width = min(max_width, terminal_width)
            padded_columns.append([wrap(path) for path in column])

        return padded_columns

    def condense_columns(columns):
        max_column_height = max([len(col) for col in columns])
        lines = [[] for _ in range(max_column_height)]
        for column in columns:
            for line, (isdir, path) in zip(lines, column):
                line.append((isdir, path))
        for line in lines:
            for i, (isdir, path) in enumerate(line):
                if isdir:
                    console(path, bold=True, fg="blue")
                else:
                    console(path)
                if i < len(line) - 1:
                    console('  ')
            console.nl()

    if format_long:
        for path in paths:
            if path in dirs:
                console(path, bold=True, fg="blue")
            else:
                console(path)
            console.nl()

    else:
        terminal_width = console.width
        path_widths = [len(path) for path in paths]
        smallest_paths = min(path_widths)
        num_paths = len(paths)

        num_cols = min(terminal_width // (smallest_paths + 2), num_paths)
        while num_cols:
            col_height = (num_paths + num_cols - 1) // num_cols
            line_width = 0
            for col_no in range(num_cols):
                try:
                    col_width = max(path_widths[col_no * col_height: (col_no + 1) * col_height])
                except ValueError:
                    continue
                line_width += col_width
                if line_width > terminal_width:
                    break
                line_width += 2
            else:
                if line_width - 1 <= terminal_width:
                    break
            num_cols -= 1
        num_cols = max(1, num_cols)
        columns = columnize(paths, num_cols)
        condense_columns(columns)


class FS(SubCommand):
    """Manage project filesystems"""
    help = "manage project fsfilesystems"

    def add_arguments(self, parser):
        parser.add_argument(dest="fs", nargs="?", default=None, metavar="FILESYSTEM",
                            help="filesystem name")
        parser.add_argument("-l", "--location", dest="location", default=None, metavar="PATH",
                            help="location of the Moya server code")
        parser.add_argument("-i", "--ini", dest="settings", default=None, metavar="SETTINGSPATH",
                            help="path to project settings")
        parser.add_argument("--server", dest="server", default='main', metavar="SERVERREF",
                            help="server element to use")
        parser.add_argument('--ls', dest="listdir", default=None, metavar="PATH",
                            help="list files / directories")
        parser.add_argument("--tree", dest="tree", nargs='?', default=None, const='/',
                            help="display a tree view of the filesystem")
        parser.add_argument("--cat", dest="cat", default=None, metavar="PATH",
                            help="Cat a file to the console")
        parser.add_argument("--syspath", dest="syspath", default=None, metavar="PATH",
                            help="display the system path of a file")
        parser.add_argument("--open", dest="open", default=None, metavar="PATH",
                            help="open a file")
        parser.add_argument("--copy", dest="copy", metavar="DESTINATION or PATH DESTINATION", nargs='+',
                            help="copy contents of a filesystem to PATH, or a file from PATH to DESTINATION")
        parser.add_argument('--extract', dest="extract", metavar="PATH DIRECTORY", nargs=2,
                            help="copy a file from a filesystem, preserving directory structure")
        parser.add_argument("-f", "--force", dest="force", action="store_true", default=False,
                            help="force overwrite of destination even if it is not empty (with --copy)")
        return parser

    def run(self):
        args = self.args
        application = WSGIApplication(self.location,
                                      self.get_settings(),
                                      args.server,
                                      disable_autoreload=True,
                                      master_settings=self.master_settings)
        archive = application.archive

        filesystems = archive.filesystems

        fs = None
        if args.fs:
            try:
                fs = filesystems[args.fs]
            except KeyError:
                self.console.error("No filesystem called '%s'" % args.fs)
                return -1

        if args.tree is not None:
            if fs is None:
                self.console.error("Filesystem required")
                return -1
            with fs.opendir(args.tree) as tree_fs:
                tree_fs.tree()
            return

        if args.listdir:
            if fs is None:
                self.console.error("Filesystem required")
                return -1

            dir_fs = fs.opendir(args.listdir)
            file_paths = dir_fs.listdir(files_only=True)
            dir_paths = dir_fs.listdir(dirs_only=True)
            _ls(self.console, file_paths, dir_paths)

        elif args.cat:
            if fs is None:
                self.console.error("Filesystem required")
                return -1
            contents = fs.getcontents(args.cat)
            self.console.cat(contents, args.cat)

        elif args.open:
            if fs is None:
                self.console.error("Filesystem required")
                return -1

            filepath = fs.getsyspath(args.open, allow_none=True)
            if filepath is None:
                self.console.error("No system path for '%s' in filesystem '%s'" % (args.open, args.fs))
                return -1

            import subprocess
            if os.name == 'mac':
                subprocess.call(('open', filepath))
            elif os.name == 'nt':
                subprocess.call(('start', filepath), shell=True)
            elif os.name == 'posix':
                subprocess.call(('xdg-open', filepath))
            else:
                self.console.error("Moya doesn't know how to open files on this platform (%s)" % os.name)

        elif args.syspath:
            if fs is None:
                self.console.error("Filesystem required")
                return -1
            if not fs.exists(args.syspath):
                self.console.error("No file called '%s' found in filesystem '%s'" % (args.syspath, args.fs))
                return -1
            syspath = fs.getsyspath(args.syspath, allow_none=True)
            if syspath is None:
                self.console.error("No system path for '%s' in filesystem '%s'" % (args.syspath, args.fs))
            else:
                self.console(syspath).nl()

        elif args.copy:
            if fs is None:
                self.console.error("Filesystem required")
                return -1
            if len(args.copy) == 1:
                src = '/'
                dst = args.copy[0]
            elif len(args.copy) == 2:
                src, dst = args.copy
            else:
                self.console.error("--copy requires 1 or 2 arguments")
                return -1

            if fs.isdir(src):
                src_fs = fs.opendir(src)
                dst_fs = fsopendir(dst, create_dir=True)

                if not args.force and not dst_fs.isdirempty('/'):
                    response = raw_input("'%s' is not empty. Copying may overwrite directory contents. Continue? " % dst)
                    if response.lower() not in ('y', 'yes'):
                        return 0

                from fs.utils import copydir
                copydir(src_fs, dst_fs)
            else:
                with fs.open(src, 'rb') as read_f:
                    if os.path.isdir(dst):
                        dst = os.path.join(dst, os.path.basename(src))
                    try:
                        os.makedirs(dst)
                        with open(dst, 'wb') as write_f:
                            while 1:
                                chunk = read_f.read(16384)
                                if not chunk:
                                    break
                                write_f.write(chunk)
                    except IOError as e:
                        self.error('unable to write to {}'.format(dst))

        elif args.extract:
            if fs is None:
                self.console.error("Filesystem required")
                return -1
            src_path, dst_dir_path = args.extract
            src_fs = fs
            dst_fs = fsopendir(dst_dir_path, create_dir=True)

            if not args.force and dst_fs.exists(src_path):
                response = raw_input("'%s' exists. Do you want to overwrite? " % src_path)
                if response.lower() not in ('y', 'yes'):
                    return 0

            dst_fs.makedir(dirname(src_path), recursive=True, allow_recreate=True)
            with src_fs.open(src_path, 'rb') as read_file:
                dst_fs.setcontents(src_path, read_file)

        else:
            table = [[Cell("Name", bold=True),
                      Cell("Type", bold=True),
                      Cell("Location", bold=True)]]

            if fs is None:
                list_filesystems = filesystems.items()
            else:
                list_filesystems = [(args.fs, fs)]

            for name, fs in sorted(list_filesystems):

                if isinstance(fs, MultiFS):
                    location = '\n'.join(mount_fs.desc('/') for mount_fs in fs.fs_sequence)
                    fg = "yellow"
                elif isinstance(fs, MountFS):
                    mount_desc = []
                    for path, dirmount in fs.mount_tree.items():
                        mount_desc.append('%s->%s' % (path, dirmount.fs.desc('/')))
                    location = '\n'.join(mount_desc)
                    fg = "magenta"
                else:
                    syspath = fs.getsyspath('/', allow_none=True)
                    if syspath is not None:
                        location = syspath
                        fg = "green"
                    else:
                        try:
                            location = fs.desc('/')
                        except FSError as e:
                            location = text_type(e)
                            fg = "red"
                        else:
                            fg = "blue"
                table.append([Cell(name),
                             Cell(type(fs).__name__),
                             Cell(location, bold=True, fg=fg)
                              ])
            self.console.table(table, header=True)
