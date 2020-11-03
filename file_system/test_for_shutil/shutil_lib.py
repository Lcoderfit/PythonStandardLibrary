import tempfile
import tarfile
import sys
import logging
import pathlib
import pprint
import os
import glob
import io
import shutil
import subprocess
from file_system.os_lib import extra_recursion_remove_path


def shutil_copyfile():
    """复制文件, 会打开输入文件进行读取，所以某些特殊文件（设备节点）不能复制为新的特殊文件"""
    print("before: ", glob.glob(r"*\*shutil.*"))
    shutil.copyfile(r"test_for_shutil\test_for_shutil.txt", r"test_for_shutil\test_for_shutil.copy.txt")
    print("Alter: ", glob.glob(r"*\*shutil.*"))
    r"""
shutil_copyfile: 
before:  ['test_for_shutil\\test_for_shutil.txt']
Alter:  ['test_for_shutil\\test_for_shutil.copy.txt', 'test_for_shutil\\test_for_shutil.txt']
    """


class VerboseStringIO(io.StringIO):
    def read(self, n=-1):
        next_text = io.StringIO.read(self, n)
        print("read({}) got {} bytes".format(n, len(next_text)))
        return next_text


def shutil_copyfileobj():
    """传入文件句柄进行复制"""
    lorem_ipsum = """
    Lorem ipsum dolor sit amet , consectetuer
    adipiscing elit. Vestibulum aliquam mollis dolor. Donec
    vulputate nunc ut diam . Ut rutrum mi vel sem. Vestibulum
    ante ipsum.
    """
    print("default: ")
    input_param = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    # 默认使用2^14次方（16384）来读取
    shutil.copyfileobj(input_param, output)

    print()

    print("All at once: ")
    input_param = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    # 一次性读取所有输入
    shutil.copyfileobj(input_param, output, -1)

    print()

    print("blocks of 256:")
    input_param = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    # 指定读取读取的块大小为256
    shutil.copyfileobj(input_param, output, 256)
    """
shutil_copyfileobj: 
default: 
read(16384) got 189 bytes
read(16384) got 0 bytes

All at once: 
read(-1) got 189 bytes
read(-1) got 0 bytes

blocks of 256:
read(256) got 189 bytes
read(256) got 0 bytes
    """


def shutil_copy():
    """如果指定的目标为一个目录，则复制后的文件会存放在该目录下, 复制后的文件权限与内容也与原文件一致, 但访问时间和修改时间不一样"""
    print("Before: ", glob.glob("test_for_shutil/*"))
    shutil.copy("shutil_lib.py", "test_for_shutil")
    print("After: ", glob.glob("test_for_shutil/*"))
    """
shutil_copy: 
Before:  ['test_for_shutil\\test_for_shutil.copy.txt', 'test_for_shutil\\test_for_shutil.txt']
After:  ['test_for_shutil\\shutil_lib.py', 'test_for_shutil\\test_for_shutil.copy.txt', 'test_for_shutil\\test_for_shutil.txt']
    """


def show_file_info(file_name):
    stat_info = os.stat(file_name)
    print("mode: ", stat_info.st_mode)
    print("create time: ", stat_info.st_ctime)
    print("access: ", stat_info.st_atime)
    print("modified time: ", stat_info.st_mtime)


def shutil_copy2():
    """复制后的特性与原文件一模一样"""
    print("source: ")
    show_file_info("os_lib.py")

    shutil.copy2("os_lib.py", "test_for_shutil")
    print("dest: ")
    show_file_info("test_for_shutil/os_lib.py")
    """
shutil_copy2: 
source: 
mode:  33206
create time:  1604370593.946
access:  1604370593.946
modified time:  1604370593.946
dest: 
mode:  33206
create time:  1604385257.103
access:  1604370593.946
modified time:  1604370593.946
    """


def shutil_copymode():
    """将权限从一个文件复制到另一个文件"""
    if os.path.exists("test_for_shutil/file_to_change.txt"):
        # 强制删除系统文件
        # os.system(r"del 'test_for_shutil\file_to_change.txt' /F")
        os.chmod("test_for_shutil/file_to_change.txt", 0o666)
        os.remove("test_for_shutil/file_to_change.txt")
    with open("test_for_shutil/file_to_change.txt", "wt") as f:
        f.write("content")
    os.chmod("test_for_shutil/file_to_change.txt", 0o444)

    print("before: ", oct(os.stat("test_for_shutil/file_to_change.txt").st_mode))

    shutil.copymode("shutil_lib.py", "test_for_shutil/file_to_change.txt")
    print("alter: ", oct(os.stat("test_for_shutil/file_to_change.txt").st_mode))
    """
shutil_copymode: 
before:  0o100444
alter:  0o100666
    """


def shutil_copystat():
    """复制文件的其他属性"""
    with open("test_for_shutil/file_to_change.txt", "wt") as f:
        f.write("content")
    os.chmod("test_for_shutil/file_to_change.txt", 0o444)

    print("before: ")
    show_file_info("test_for_shutil/file_to_change.txt")

    shutil.copystat("shutil_lib.py", "test_for_shutil/file_to_change.txt")
    print("after: ")
    show_file_info("test_for_shutil/file_to_change.txt")
    """
shutil_copystat: 
before: 
mode:  33060
create time:  1604386294.72
access:  1604386901.831
modified time:  1604386901.834
after: 
mode:  33206
create time:  1604386294.72
access:  1604386901.378
modified time:  1604386901.379
    """


def shutil_copytree():
    """一个目录下的文件复制到另一个目录，目标目录必须不存在"""
    extra_recursion_remove_path("test_for_shutil_copytree")
    print("before: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))

    shutil.copytree(r"dir", "test_for_shutil_copytree")

    print("after: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))
    r"""
shutil_copytree: 
before: 
[]
after: 
['test_for_shutil_copytree\\file.txt',
 'test_for_shutil_copytree\\file1.txt',
 'test_for_shutil_copytree\\file2.txt',
 'test_for_shutil_copytree\\filea.txt',
 'test_for_shutil_copytree\\fileb.txt',
 'test_for_shutil_copytree\\file[.txt',
 'test_for_shutil_copytree\\subdir']
    """


def verbose_copy(src, dst):
    """复制文件（属性和内容均一致）"""
    print("copying {!r} to {!r}".format(src, dst))
    return shutil.copy2(src, dst)


def get_dirs(dir_name):
    """获取目录下的所有目录（而不是文件）"""
    dir_list = []
    for file in os.listdir(dir_name):
        if os.path.isdir(file):
            dir_list.append(file)
    return dir_list


def shutil_copytree_verbose():
    """精确控制目录下要复制的文件, ignore_patterns为关键字参数"""
    extra_recursion_remove_path("test_for_shutil_copytree")
    print("before: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))
    print()

    dir_list = get_dirs("../file_system")
    dir_list.append("*.txt")
    # 复制时过滤掉file_system下的目录、和.txt文件，只复制py文件
    # 第二个参数("test_for_shutil_copytree")必须是一个不存在的目录
    shutil.copytree(
        r"..\file_system", "test_for_shutil_copytree",
        copy_function=verbose_copy,
        ignore=shutil.ignore_patterns(*dir_list, "*.txt")
    )
    print()
    print("after: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))
    r"""
before: 
[]

copying '..\\file_system\\fnmatch_lib.py' to 'test_for_shutil_copytree\\fnmatch_lib.py'
copying '..\\file_system\\global_lib.py' to 'test_for_shutil_copytree\\global_lib.py'
copying '..\\file_system\\linecache_lib.py' to 'test_for_shutil_copytree\\linecache_lib.py'
copying '..\\file_system\\os_lib.py' to 'test_for_shutil_copytree\\os_lib.py'
copying '..\\file_system\\pathlib_lib.py' to 'test_for_shutil_copytree\\pathlib_lib.py'
copying '..\\file_system\\shutil_lib.py' to 'test_for_shutil_copytree\\shutil_lib.py'
copying '..\\file_system\\tempfile_lib.py' to 'test_for_shutil_copytree\\tempfile_lib.py'
copying '..\\file_system\\unit_test.py' to 'test_for_shutil_copytree\\unit_test.py'
copying '..\\file_system\\__init__.py' to 'test_for_shutil_copytree\\__init__.py'

after: 
['test_for_shutil_copytree\\fnmatch_lib.py',
 'test_for_shutil_copytree\\global_lib.py',
 'test_for_shutil_copytree\\linecache_lib.py',
 'test_for_shutil_copytree\\os_lib.py',
 'test_for_shutil_copytree\\pathlib_lib.py',
 'test_for_shutil_copytree\\shutil_lib.py',
 'test_for_shutil_copytree\\tempfile_lib.py',
 'test_for_shutil_copytree\\unit_test.py',
 'test_for_shutil_copytree\\__init__.py']
    """


def shutil_rmtree():
    """删除文件或目录， 即使文件下有很多嵌套子目录依旧会删除"""
    print("before: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))

    shutil.rmtree("test_for_shutil_copytree")

    print("after: ")
    pprint.pprint(glob.glob("test_for_shutil_copytree/*"))
    r"""
shutil_rmtree: 
before: 
['test_for_shutil_copytree\\fnmatch_lib.py',
 'test_for_shutil_copytree\\global_lib.py',
 'test_for_shutil_copytree\\linecache_lib.py',
 'test_for_shutil_copytree\\os_lib.py',
 'test_for_shutil_copytree\\pathlib_lib.py',
 'test_for_shutil_copytree\\shutil_lib.py',
 'test_for_shutil_copytree\\tempfile_lib.py',
 'test_for_shutil_copytree\\unit_test.py',
 'test_for_shutil_copytree\\__init__.py']
after: 
[]
    """


def shutil_move():
    """将文件从一个目录移动到另一个目录, shutil.move类似于unix的move命令，如果其参数为两个文件，则表示重命名"""
    # 创建一个文件
    p = pathlib.Path("test_file/file")
    p.touch()

    if os.path.exists("test_for_shutil/file"):
        os.remove("test_for_shutil/file")

    print("before: ", glob.glob("test_for_shutil/*"))
    # 如果文件已存在，则会报错
    shutil.move("test_file/file", "test_for_shutil")
    print("after: ", glob.glob("test_for_shutil/*"))
    r"""
shutil_move: 
before:  ['test_for_shutil\\file_to_change.txt', 'test_for_shutil\\os_lib.py', 'test_for_shutil\\shutil_lib.py', 'test_for_shutil\\test_for_shutil.copy.txt', 'test_for_shutil\\test_for_shutil.txt']
after:  ['test_for_shutil\\file', 'test_for_shutil\\file_to_change.txt', 'test_for_shutil\\os_lib.py', 'test_for_shutil\\shutil_lib.py', 'test_for_shutil\\test_for_shutil.copy.txt', 'test_for_shutil\\test_for_shutil.txt']
    """


def shutil_which():
    """查找文件???????????"""
    mode = os.F_OK | os.R_OK
    print(shutil.which("os_lib.py", mode=mode, path=r"D:\PrivateProject\Python-Tags\PythonStandardLibrary"))
    print(shutil.which("file"))
    print(shutil.which("InstallPlace"))
    """
shutil_which: 
.\os_lib.py
None
None
    """


def shutil_get_achive_formats():
    """返回当前系统上所支持的所有归档文件的格式"""
    for format_param, description in shutil.get_archive_formats():
        print("{:5}: {}".format(format_param, description))
    """
shutil_get_achive_formats: 
bztar: bzip2'ed tar-file
gztar: gzip'ed tar-file
tar  : uncompressed tar file
xztar: xz'ed tar-file
zip  : ZIP file
    """


def shutil_make_achive():
    """
    1.创建一个归档文件, 默认将当前文件所在的目录中的所有文件（和目录）进行归档，root_dir表示当前要进入的目录，可以通过root_dir参数指定需要归档的目录；
    生成的归档文件将保存在当前目录下,
    2.即使当前目录下有同名的压缩包，程序运行也不会报错，而相当于更新那个压缩包
    3.base_dir参数相当于在root_dir所指定的文件系统下，将对应路径的文件或目录放入压缩包中
    """
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.DEBUG,
    )
    logger = logging.getLogger("pymotw")

    print("create achive: ")
    # 第一个参数表示归档后的名称，第二个参数表示归档的格式，系统所支持的归档格式可以用shutil.get_achive_formats()查看
    shutil.make_archive(
        "make_achive", "tar",
        root_dir="../data_compression_and_archive/",
        base_dir="here",
        logger=logger
    )
    print("\nachive contents: ")
    with tarfile.open("make_achive.tar", "r") as t:
        for n in t.getnames():
            print(n)
    # 将该归档文件移动到test_for_shutil目录下
    shutil.move("make_achive.tar", "test_for_shutil/make_achive.tar")
    r"""root_dir进入"../data_compression_and_archive/"文件系统，在该系统下将“here”文件夹放入归档文件中
shutil_make_achive: 
create achive: 
changing into '../data_compression_and_archive/'
Creating tar archive
changing back to 'D:\PrivateProject\Python-Tags\PythonStandardLibrary\file_system'

achive contents: 
here
here/__init__.py
here/a.txt
here/inhere
here/inhere/inhe.py
here/tarfile_lib.py
    """


def shutil_get_unpack_formats():
    """返回当前系统支持的解包格式"""
    # exts表示归档格式对应的后缀名
    for formats, exts, description in shutil.get_unpack_formats():
        print("{:5}: {}, names ending in {}".format(
            formats, description, exts
        ))


def shutil_unpack_achive():
    """解压归档文件"""
    # 创建临时文件用于存放归档文件，with语句结束后临时文件会被删除
    with tempfile.TemporaryDirectory() as d:
        print("Unpacking achive: ")
        shutil.unpack_archive(
            r"test_for_shutil/make_achive.tar",
            extract_dir=d
        )
        print("\nCreated: ")
        for extracted in pathlib.Path(d).rglob("*"):
            print(str(extracted))

    # print("Unpacking achive: ")
    # # 如果解压的文件不存在会报错, 如果解压之后的文件与当前目录下的某个文件重名了，则不会覆盖，也不会报错。
    # shutil.unpack_archive(
    #     r"test_for_shutil/make_achive.tar",
    #     extract_dir="test_file"
    # )
    # print("\nCreated: ")
    # for extracted in pathlib.Path("test_file").rglob("*"):
    #     print(str(extracted))


def shutil_disk_usage():
    """查看文件系统（磁盘）的可用空间"""
    # 总空间，已使用的空间，剩余空间
    total_b, use_b, free_b = shutil.disk_usage(".")
    gib = 2 ** 30   # gibibyte
    gb = 10 ** 9      # gigabyte
    print("total: {:6.2f}GB   {:6.2f}GiB".format(total_b / gb, total_b / gib))
    print("use_b: {:6.2f}GB   {:6.2f}GiB".format(use_b / gb, use_b / gib))
    print("free_b: {:6.2f}GB   {:6.2f}GiB".format(free_b / gb, free_b / gib))


if __name__ == '__main__':
    # 复制、移动、删除、重命名、查找文件
    print("\nshutil_copyfile: ")
    shutil_copyfile()

    print("\nshutil_copyfileobj: ")
    shutil_copyfileobj()

    print("\nshutil_copy: ")
    shutil_copy()

    print("\nshutil_copy2: ")
    shutil_copy2()

    print("\nshutil_copymode: ")
    shutil_copymode()

    print("\nshutil_copystat: ")
    shutil_copystat()

    print("\nshutil_copytree: ")
    shutil_copytree()

    print("\nshutil_copytree_verbose: ")
    shutil_copytree_verbose()

    print("\nshutil_rmtree: ")
    shutil_rmtree()

    print("\nshutil_move: ")
    shutil_move()

    # 这个which函数感觉没啥用。。。。（用glob可以实现文件匹配和查找）
    print("\nshutil_which: ")
    shutil_which()

    print("\nshutil_get_achive_formats: ")
    shutil_get_achive_formats()

    print("\nshutil_make_achive: ")
    shutil_make_achive()

    print("\nshutil_get_unpack_formats: ")
    shutil_get_unpack_formats()

    print("\nshutil_unpack_achive: ")
    shutil_unpack_achive()

    print("\nshutil_disk_usage: ")
    shutil_disk_usage()
