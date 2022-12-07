import sys

lines_in = [line.strip() for line in sys.stdin]

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def register_subdir(self, name):
        new_dir = Dir(name, self)
        self.dirs.append(new_dir)

        return new_dir

    def register_file(self, name, size):
        self.files.append(File(name, size))

    def get_size(self):
        file_size = sum([file.size for file in self.files])
        dir_size = sum([directory.get_size() for directory in self.dirs])

        return file_size + dir_size

dirs = Dir('/', None)
current_dir = dirs
pointer = 1

while pointer < len(lines_in):
    line = lines_in[pointer]

    if line.startswith('$'):
        if line.startswith('$ cd'):
            if line == '$ cd /':
                current_dir = dirs
            elif line == '$ cd ..':
                current_dir = current_dir.parent
            else:
                cd_into = line.split(' ')[2]
                current_dir = next((directory for directory in current_dir.dirs if directory.name == cd_into))
        if line.startswith('$ ls'):
            while not lines_in[pointer + 1].startswith('$'):
                pointer += 1
                next_line = lines_in[pointer]
                if next_line.startswith('dir'):
                    current_dir.register_subdir(next_line.split(' ')[1])
                else:
                    f_size, f_name = next_line.split(' ')
                    current_dir.register_file(f_name, int(f_size))

                if pointer + 1 >= len(lines_in):
                    break
    pointer += 1

pt1_total = 0
pt2 = 1e20

total = dirs.get_size()

def crawl(dir):
    global pt1_total
    global pt2
    s = dir.get_size()
    if s <= 100000:
        pt1_total += dir.get_size()

    if total - (70000000 - 30000000) < s < pt2:
        pt2 = s
    for sub_dir in dir.dirs:
        crawl(sub_dir)

crawl(dirs)
print('part 1', pt1_total)
print('part 2', pt2)