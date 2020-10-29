import os
import tempfile
import linecache
import pprint

# 一共只有15行,最后面的"""所在的一行是不包含在内的
lorem = """1Lorem ipsum dolor sit amet. consectetuer
2adipiscing elit. Vivamus eget elit. In posuere mi non
3risus. 例auris id quam posuere lectus sollicitudin
4varius. Praesent at mi. Nunc eu velit. Sed augue massa.
5fermentum id. nonummy a , nonummy sit amet , ligula. Curabitur
6eros pede, egestas at, ultricies ac , apellentesque eu, tellus.
7Sed sed odio sed mi luctus mollis. Integer et nulla ac augue

9convallis accumsan. Ut felis. Donec lectus sapien, elementum
10nec , condimentum ac, interdum non, tellus. Aenean viverra ,
11mauris vehicula semper porttitor. ipsum odio consectetuer
12lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus ,
13aliquam non , egestas a, nonummy et, erat. Vivamus sagittis
14porttitor eros.

"""


def make_tempfile():
    """创建临时文件"""
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, "w", encoding="utf8") as f:
        f.write(lorem)
    return temp_file_name


def cleanup(filename):
    """删除文件"""
    os.unlink(filename)


def linecache_getline():
    """获取文件中的特定行"""
    file_name = make_tempfile()
    print("source: ")
    # 取第五行的数据
    print("{}".format(lorem.split("\n")[4]))

    print("linecache: ")
    # 返回值会包含末尾的一个空行, 如果文本内容为空，则会返回一个空字符
    print("{!r}".format(linecache.getline(file_name, 5)))
    cleanup(file_name)
    """
source: 
fermentum id. nonummy a , nonummy sit amet , ligula. Curabitur
linecache: 
'fermentum id. nonummy a , nonummy sit amet , ligula. Curabitur\n'
    """


def linecache_empty_line():
    """如果该行不存在，则返回一个空字符，如果该行为一个空行，则返回一个换行符"""
    file_name = make_tempfile()
    print("source: ")
    print("{!r}".format(lorem.split("\n")[7]))

    print("linecache: ")
    print("{!r}".format(linecache.getline(file_name, 8)))
    print("{!r}".format(linecache.getline(file_name, 18)))
    print("{!r}".format(linecache.getline(file_name, 15)))
    """
source: 
''
linecache: 
'\n'
''
'\n'
    """


def linecache_missing_file():
    """读取不存在的文件时，不会报错，会返回一个空字符"""
    no_such_file = linecache.getline("not_exist_file.txt", 1)
    print("{!r}".format(no_such_file))
    """
''
    """


def linecache_path_search():
    """读取内置模块文件"""
    # 如果文件名无法在当前目录中找到，则会去sys.path目录下查找对应的内置模块文件
    module_line = linecache.getline("linecache.py", 3)
    print("Module: ")
    print(repr(module_line))

    file_src = linecache.__file__
    if file_src.endswith(".pyc"):
        file_src = file_src[:-1]
    print("\nFile: ")
    with open(file_src, "r") as f:
        file_line = f.readlines()[2]
    print(repr(file_line))


if __name__ == '__main__':
    # 用于查找一个文件中的指定行, 通过索引一个list来返回请求的行
    print("\nlinecache_getline: ")
    linecache_getline()

    print("\nlinecache_empty_line: ")
    linecache_empty_line()

    print("\nlinecache_missing_file: ")
    linecache_missing_file()

    print("\nlinecache_path_search: ")
    linecache_path_search()
