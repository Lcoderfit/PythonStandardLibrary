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


def pathlib_parts():
    """将路径根据路径分隔符分隔，得到一个元组"""
    path = pathlib.WindowsPath(r"D:\lcoderfit\fuck")
    part_list = path.parts
    print(part_list)

    """
    ('D:\\', 'lcoderfit', 'fuck')
    """


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

    r"""
    home:  C:\Users\Lcoderfit
    cwd:  E:\SocialProject\Learn-Tags\PythonStandardLibrary\file_system
    """


def pathlib_iterdir():
    """访问目录列表, 如果Path不指示一个目录，会产生NotADirectoryError
    如果指示的目录不存在，会抛出一个FileNotFoundError
    """
    p = pathlib.Path(".")
    for f in p.iterdir():
        print(f)

    r"""
    os_lib.py
    pathlib_lib.py
    """


def pathlib_global():
    """通过匹配模式找到对应的文件"""
    p = pathlib.Path(".")
    for f in p.glob("*.py"):
        print(f)

    r"""
os_lib.py
pathlib_lib.py
    """


def pathlib_rglobal():
    """支持递归扫描"""
    p = pathlib.Path(".")
    for f in p.rglob("*.py"):
        print(f)

    """
os_lib.py
pathlib_lib.py
test_for_rglobal\test_for_rglobal.py
    """


def path_read_write():
    """读写文件"""
    f = pathlib.Path("os_lib.py")
    f.write_bytes("This is function path_read_write".encode("utf-8"))
    with f.open('r', encoding="utf-8") as handle:
        print("read from open(): {!r}".format(handle.read()))

    print("read_text(): {!r}".format(f.read_text("utf-8")))
    print(f.read_bytes())
    print(f.read_bytes().decode("utf-8"))

    """
read from open(): 'This is function path_read_write'
read_text(): 'This is function path_read_write'
b'This is function path_read_write'
This is function path_read_write
    """


def pathlib_mkdir():
    """创建文件, 如果文件已存在，则会产生一个FileExistsError"""
    # p = pathlib.Path("a")
    # print("Creating {}".format(p))
    # p.mkdir()


def pathlib_symlink_to():
    """创建符号链接"""
    p = pathlib.Path("first_link")
    p.symlink_to("test_for_rglobal/test_for_rglobal.py")
    print(p)
    print(p.resolve().name)


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

    print("\npathlib_parts")
    pathlib_parts()

    print("\npathlib_parent: ")
    pathlib_parent()

    print("\n pathlib_properties: ")
    pathlib_properties()

    print("\npathlib_convenience: ")
    pathlib_convenience()

    # 访问文件系统中存在的目录
    print("\npathlib_iterdir: ")
    pathlib_iterdir()

    print("\npathlib_global: ")
    pathlib_global()

    print("\npathlib_rglobal: ")
    pathlib_rglobal()

    # 读写文件
    print("\npath_read_write: ")
    path_read_write()

    # 创建目录和符号链接
    print("\npathlib_mkdir: ")
    pathlib_mkdir()

    print("\npathlib_symlink_to: ")
    pathlib_symlink_to()


