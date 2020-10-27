import glob
import os
import pathlib


def extra_recursion_remove_path(dir_path="test_for_recursion"):
    """递归删除目录及其子文件或目录"""
    # if os.path.exists(dir_path):
    #     for file_name in os.listdir(dir_path):
    #         os.remove(os.path.join(dir_path, file_name))
    #     os.rmdir(dir_path)
    # os.mkdir(dir_path)

    if not os.path.exists(dir_path):
        return
    for file_name in os.listdir(dir_path):
        operate_file = os.path.join(dir_path, file_name)
        if os.path.isdir(operate_file):
            extra_recursion_remove_path(operate_file)
        else:
            os.remove(operate_file)
    os.rmdir(dir_path)


def glob_mkfile():
    # 会报权限错误
    # p = pathlib.Path("dir")
    # if p.exists():
    #     for f in p.iterdir():
    #         if f.is_file() or f.is_symlink():
    #             f.unlink()
    #         elif f.is_dir():
    #             f.rmdir()
    # ???????????????????????p.unlink()报错----------------------
    #     p.unlink()
    # p.mkdir()

    path = "dir"
    extra_recursion_remove_path(path)

    p = pathlib.Path(path)
    p.mkdir()

    file_list = [
        "file.txt", "file1.txt", "file2.txt", "filea.txt",
        "fileb.txt", "file[.txt",
        "subdir", "subdir/subfile.txt"
    ]
    for f in file_list:
        if "." in f:
            (p / f).touch()
        else:
            (p / f).mkdir()


def glob_asterisk():
    """星号匹配"""
    # glob函数不会递归搜索目录，返回的结果不会排序，所以需要显示处理
    for name in sorted(glob.glob("dir/*")):
        print(name)
    r"""
dir\file.txt
dir\file1.txt
dir\file2.txt
dir\file[.txt
dir\filea.txt
dir\fileb.txt
dir\subdir
    """


def glob_subdir():
    """列出子目录, *号匹配一个文件名段中的0个或多个字符"""
    print("Named explicitly")
    for name in sorted(glob.glob("dir/subdir/*")):
        print("{}".format(name))

    for name in sorted(glob.glob("dir/*/*")):
        print("{}".format(name))

    r"""
Named explicitly
dir/subdir\subfile.txt
dir\subdir\subfile.txt
    """


def glob_question():
    """?匹配任意的单个字符"""
    for name in sorted(glob.glob("dir/file?.txt")):
        print("{}".format(name))

    r"""
dir\file1.txt
dir\file2.txt
dir\file[.txt
dir\filea.txt
dir\fileb.txt
    """


def glob_charrange():
    """[]匹配字符区间"""
    for name in sorted(glob.glob("dir/*[0-9].*")):
        print(name)
    r"""
dir\file1.txt
dir\file2.txt
    """


def glob_escape():
    """匹配特殊字符"""
    specials = "?*["
    for char in specials:
        pattern = "dir/*" + glob.escape(char) + ".txt"
        print("Searching for :{!r}".format(pattern))
        for name in sorted(glob.glob(pattern)):
            print("{}".format(name))
        print()

    # 等效于pattern = "dir/*" + glob.escape(char) + ".txt"
    # for name in sorted(glob.glob(pattern)) .....
    for name in sorted(glob.glob("dir/*[[].*")):
        print("{}".format(name))

    r"""
Searching for :'dir/*[?].txt'

Searching for :'dir/*[*].txt'

Searching for :'dir/*[[].txt'
dir\file[.txt

dir\file[.txt
    """


if __name__ == '__main__':
    # print("\nglob_mkfile: ")
    # glob_mkfile()dir

    print("\nglob_mkfile: ")
    glob_mkfile()

    print("\nglob_asterisk: ")
    glob_asterisk()

    print("\nglob_subdir: ")
    glob_subdir()

    print("\nglob_question: ")
    glob_question()

    print("\nglob_charrange: ")
    glob_charrange()

    print("\nglob_escape: ")
    glob_escape()
