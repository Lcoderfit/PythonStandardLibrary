import os


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


# splittext(): 通过扩展名分隔符进行分隔
def os_path_splitext():
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
        ("one", "two", "three"),    # one\two\three
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
