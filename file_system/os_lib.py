import os
import datetime
import time


def os_path_sep():
    print(os.path.sep)
    print(os.path.extsep)
    print(os.path.pardir)
    print(os.path.curdir)


def os_path_split():
    paths = [
        "/one/two/three",
        "/one/two/three/",
        "/",
        ".",
        "",
    ]

    # !r表示将参数传入到repr函数中， split会根据最右边的"/"进行分割
    for path in paths:
        print("{!r:>17}: {}".format(path, os.path.split(path)))


def os_path_basename_and_dirname():
    paths = [
        "/one/two/three",
        "/one/two/three/",
        "/",
        ".",
        ""
    ]

    # basename是通过最右边的“/”分割成的左右两部分的右部分
    # dirname是通过最右边的“/”分割成的左右两部分的左部分
    for path in paths:
        print("{!r:>17}: {}".format(path, os.path.basename(path)))

    for path in paths:
        print("{!r:>17}: {}".format(path, os.path.dirname(path)))


def os_path_splitext():
    """通过扩展名分隔符进行分隔"""
    paths = [
        "/one/two/three.txt",
        "/one/two.py",
        ".",
        "/",
        "a.tar.gz"
    ]

    for path in paths:
        print("{!r:>17}: {}".format(path, os.path.splitext(path)))


def os_path_commonprefix():
    """多个路径的公共前缀"""
    paths = [
        "/one/two/three",
        "/one/two/three_bool",
        "/one/two/three/fourth"
    ]

    # 注意，在路径字符串中，如果出现像three_bool这种，也会认为与其他另个路径具有共同部分three
    print(os.path.commonprefix(paths))


def os_path_commonpath():
    """多个路径的父路径"""
    paths = [
        "/one/two/three",
        "/one/two/three_boll",
        "/one/two/three/four"
    ]

    # 结果为: /one/two(unix系统) \one\two（windows系统）
    print(os.path.commonpath(paths))


def os_path_join():
    """拼接路径"""
    paths = [
        ("one", "two", "three"),  # one\two\three
        ("\\", "one", "\\two", "three"),  # \one\two\three
        ("/", "/one", "two", "three"),  # /one\two\three
        ("/one", "/two", "/three"),  # /three
        ("\\one", "two", "\\three")
    ]

    # join函数的参数必须是字符串（传入多个字符串就是将这多个字符串拼接起来）
    # 如果参数最前面有以os.sep(系统文件名分隔符)开头，则会丢弃前面的参数
    for path in paths:
        print("{!r:>17}: {},    规范化路径{}".format(path, os.path.join(*path), os.path.normpath(os.path.join(*path))))


def os_path_expanduser():
    """扩展成用户路径"""
    paths = [
        "",
        "lcoder",
        "lcoderfit"
    ]

    # 如果用户主目录无法找到，则直接返回原来的字符串
    for path in paths:
        path = "~" + path
        print("{!r:>17}: {}".format(path, os.path.expanduser(path)))

    r"""
                  '~': C:\Users\viruser.v-desktop
        '~lcoder': C:\Users\lcoder
     '~lcoderfit': C:\Users\lcoderfit
    """


def os_path_expandvars():
    """扩展环境变量"""
    os.environ["lcoder"] = "D:\\software\\python"

    # 输出环境变量
    print(os.path.expandvars("$lcoder"))
    # 扩展环境变量
    print(os.path.expandvars("expand-\$lcoder"))
    """
    D:\software\python
    expand\D:\software\python
    """


def os_path_normpath():
    """规范化路径"""
    paths = [
        "//one/../two/.../three",
        "/one//two/./three",
        "one/two//three"
    ]

    # 将路径规范化，去除多余的分隔符, join得到的结果可能会有多余的分隔符，可以先用join拼接路径，然后用normpath规范化
    for path in paths:
        print("{!r:>17}: {}".format(path, os.path.normpath(path)))


def os_path_abspath():
    """将相对路径转换为绝对路径"""
    os.chdir("C:\\")
    paths = [
        ".",
        "..",
        "/one/two/three",
        "./one/two",
    ]

    for path in paths:
        print("{!r:>21}: {!r}".format(path, os.path.abspath(path)))


def os_path_properties():
    """获取文件属性"""
    print("File: ", __file__)
    # 访问时间, 时间戳转英文日期，用time.ctime, 时间戳转数字日期，用datetime.datetime.fromtimestamp
    print("access time: ", time.ctime(os.path.getatime(__file__)),
          datetime.datetime.fromtimestamp(os.path.getatime(__file__)))
    print("modified time: ", datetime.datetime.fromtimestamp(os.path.getmtime(__file__)))
    # 创建时间
    print("create time: ", datetime.datetime.fromtimestamp(os.path.getctime(__file__)))
    print("size: ", datetime.datetime.fromtimestamp(os.path.getsize(__file__)))


def os_path_file():
    """输出__file__(当前文件)的路径"""
    # 绝对路径： E:/SocialProject/Learn-Tags/PythonStandardLibrary/file_system/os_lib.py
    print(__file__)
    # 不包含文件名称的路径： E:/SocialProject/Learn-Tags/PythonStandardLibrary/file_system
    print(os.path.dirname(__file__))
    # 文件名称： os_lib.py
    print(os.path.basename(__file__))


def os_path_tests():
    """测试文件是否存在"""
    paths = [
        __file__,
        os.path.dirname(__file__),
        "D:",
        r"E:\MySQL.lnk",
        r"E:\SQL必知必会（第4版）.pdf.lnk"
    ]

    # windows系统中快捷方式都有一个lnk后缀被隐藏显示了
    for path in paths:
        path = os.path.normpath(path)
        print("FIle     :", path)
        print("is abs?  :", os.path.isabs(path))
        print("is File? :", os.path.isfile(path))
        print("is dir?  :", os.path.isdir(path))
        print("is link? :", os.path.islink(path))
        print("is MountPoint?:", os.path.ismount(path))
        print("exists?  :", os.path.exists(path))
        print("is link exists :", os.path.lexists(path))
        print()


if __name__ == "__main__":
    os_path_split()

    print()
    os_path_basename_and_dirname()

    print("\nos_path_splitext:")
    os_path_splitext()

    print("\nos_path_commonprefix:")
    os_path_commonprefix()

    print("\nos_path_commonpath:")
    os_path_commonpath()

    print("\nos_path_join：")
    os_path_join()

    print("\nos_path_expanduser:")
    os_path_expanduser()

    print("\nos_path_expandvars:")
    os_path_expandvars()

    print("\nos_path_normpath:")
    os_path_normpath()

    print("\nos_path_abspath:")
    os_path_abspath()

    print("\nos_path_properties: ")
    os_path_properties()

    print("\nos_path_tests: ")
    os_path_tests()
