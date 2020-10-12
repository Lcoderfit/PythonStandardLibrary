import pathlib


def pathlib_operate():
    """建立路径"""
    usr = pathlib.WindowsPath("lcoder")
    # 会进行字符串拼接
    software = usr / "software"
    print(software)

    root = usr / ".."
    print(root)

    # 通过"/"拼接后的root也可以进行“/”拼接
    k = root / "here"
    print(k)

    # 无法对路径进行规范化，如果后面连接的字符串以os.sep开头，则会删除前面的部分
    # \etc
    b = k / "/etc/"
    print(b)


def pathlib_resove():
    """规范化路径"""
    usr = pathlib.WindowsPath(r"D:")
    path = usr / ".." / "lcoder"
    path = path.resolve()
    print(path)
    print((usr / "\lcoder").resolve())
    # 如果是link则会显示目标的路径
    print((usr / "\MySQL.lnk").resolve())


def pathlib_joinpath():
    """在路径段不可知的情况下创建路径"""
    paths = [
        "one",
        "two"
    ]
    base = pathlib.WindowsPath("D:")
    print(base.joinpath(*paths))


def pathlib_existing():
    """根据现有路径创建相似的路径"""
    path = pathlib.WindowsPath(r"D:\lcoder\a.py")
    print(path)
    path = path.with_name("a.go")
    print(path)
    path = path.with_suffix(".conf")
    print(path)


def pathlib_parent():
    """不断向上迭代获取父目录"""
    path = pathlib.WindowsPath(r"D:\one\two\three.py")
    # D:\one\two
    print(path.parent)

    """
    D:\one\two
    D:\one
    D:\
    """
    for p in path.parents:
        print(p)


def pathlib_properties():
    """通过路径对象的属性来访问其他部分"""
    """
    path:  D:\one\two\target.py
    name:  target.py
    suffix:  .py
    stem:  target
    """
    p = pathlib.WindowsPath(r"D:\one\two\target.py")
    print("path: ", p)
    # 路径的最后一部分
    print("name: ", p.name)
    # 路径最后一部分的后缀
    print("suffix: ", p.suffix)
    # 路径中最后一部分(不包含后缀)
    print("stem: ", p.stem)

    print()
    """
    path:  D:\one\two\target
    name:  target
    suffix:  
    stem:  target
    """
    p = pathlib.WindowsPath(r"D:\one\two\target")
    print("path: ", p)
    # 路径的最后一部分
    print("name: ", p.name)
    # 路径最后一部分的后缀
    print("suffix: ", p.suffix)
    # 路径中最后一部分(不包含后缀)
    print("stem: ", p.stem)


def pathlib_convenience():
    """创建绝对路径文件系统"""
    home = pathlib.Path.home()
    # 当前文件所在路径
    cwd = pathlib.Path.cwd()
    print("home: ", home)
    print("cwd: ", cwd)


if __name__ == "__main__":
    # pathlib: 用来进行路径处理的库，可以替代os.path

    print("\npathlib_operate: ")
    pathlib_operate()

    print("\npathlib_resove: ")
    pathlib_resove()

    print("\npathlib_joinpath: ")
    pathlib_joinpath()

    print("\npathlib_existing: ")
    pathlib_existing()

    print("\npathlib_parent: ")
    pathlib_parent()

    print("\n pathlib_properties: ")
    pathlib_properties()

    print("\npathlib_convenience: ")
    pathlib_convenience()
