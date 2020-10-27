import datetime
import itertools
import os
import pathlib
import time
import stat
import sys


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


def pathlib_types():
    """检测文件类型"""
    root = pathlib.Path("test_file")
    if root.exists():
        for f in root.iterdir():
            # 如果test_file是个文件或者链接，则会删除，如果是个目录，则会调用rmdir()删除该目录
            f.unlink()
    else:
        root.mkdir()

    (root / 'file').write_text("this is a regular file", encoding='utf-8')
    # ??????????    OSError: symbolic link privilege not held
    (root / 'symlink').symlink_to('file')
    os.mkfifo(str(root / 'fifo'))

    to_scan = itertools.chain(
        root.iterdir(),
        [
            pathlib.Path('/dev/disk0'),
            pathlib.Path('/dev/console'),
        ]
    )
    hfmt = '{:18s}' + ('  {:>5} * 6')
    print(hfmt.format("Name", "File", "Dir", "Link", "FIFO", "Block", "Character"))
    print()
    # !r表示对参数调用repr函数的返回值
    fmt = '{:20s}' + ('{!r:>5} * 6')

    for f in to_scan:
        print(fmt.format(
            str(f),
            f.is_file(),
            f.is_dir(),
            f.is_symlink(),
            f.is_fifo(),
            f.is_block_device(),
            f.is_char_device(),
        ))


def pathlib_stat():
    """返回文件或链接的属性"""
    # lstat用来检查一个可能是符号链接的目标状态
    if len(sys.argv) == 1:
        filename = __file__
    else:
        filename = sys.argv[1]
    p = pathlib.Path(filename)
    stat_info = p.stat()
    print('{}'.format(filename))
    print('Size:', stat_info.st_size)
    print('Permissions:', oct(stat_info.st_mode))
    print('Owner:', stat_info.st_uid)
    print('Device: ', stat_info.st_dev)
    # 创建时间
    print("created: ", time.ctime(stat_info.st_ctime), datetime.datetime.fromtimestamp(stat_info.st_ctime))
    # 修改时间
    print("last modified: ", time.ctime(stat_info.st_mtime), datetime.datetime.fromtimestamp(stat_info.st_mtime))
    # 访问时间
    print("last accessed: ", time.ctime(stat_info.st_atime), datetime.datetime.fromtimestamp(stat_info.st_atime))

    """
    D:/PrivateProject/Python-Tags/PythonStandardLibrary/file_system/pathlib_lib.py
    Size: 5518
    Permissions: 0o100666
    Owner: 0
    Device:  1692097895
    created:  Mon Oct 26 09:46:14 2020 2020-10-26 09:46:14.449000
    last modified:  Mon Oct 26 11:11:35 2020 2020-10-26 11:11:35.660000
    last accessed:  Mon Oct 26 11:11:35 2020 2020-10-26 11:11:35.660000
    """


def pathlib_ownership():
    """访问文件所有者信息"""
    p = pathlib.Path(__file__)
    print('{} is owned by {}/{}', p, p.owner(), p.group())


def pathlib_touch():
    """创建一个文件，或者更新一个现有文件的修改时间和权限"""
    p = pathlib.Path('touched')
    if p.exists():
        print("already exists")
    else:
        print("creating new")
    p.touch()
    start = p.stat()

    time.sleep(1)
    p.touch()
    end = p.stat()

    print("Start: ", time.ctime(start.st_mtime), datetime.datetime.fromtimestamp(start.st_mtime))
    print("End: ", time.ctime(end.st_mtime), datetime.datetime.fromtimestamp(end.st_mtime))

    """
already exists
Start:  Mon Oct 26 11:43:13 2020 2020-10-26 11:43:13.565000
End:  Mon Oct 26 11:43:14 2020 2020-10-26 11:43:14.565000
    """


def pathlib_chmod():
    """修改文件的权限"""
    f = pathlib.Path("test_for_chmod.txt")
    if f.exists():
        f.unlink()
    f.touch()
    f.write_bytes("contents".encode("utf-8"))
    # 返回文件的权限
    existing_permissions = stat.S_IMODE(f.stat().st_mode)
    # 以8进制的方式输出
    print("Before: {:o}".format(existing_permissions))

    # 无法修改文件权限
    if not (existing_permissions & os.X_OK):
        print("Adding excute permission")
        # S_IXUSR: 所有者拥有执行权限
        new_permissions = existing_permissions | stat.S_IXUSR
    else:
        print("Removeing execute permission")
        new_permissions = existing_permissions ^ stat.S_IXUSR

    f.chmod(444)
    after_permissions = stat.S_IMODE(f.stat().st_mode)
    print(new_permissions)
    print(after_permissions)
    print("{:o}".format(after_permissions))

    """
Before: 666
Adding excute permission
666
    """


def pathlib_rmdir():
    """删除一个空目录，如果目录不是空的，则会弹出OSError错误, 如果删除一个不存在的目录,则会产生FileNotFoundError"""
    p = pathlib.Path("test_for_rm")
    if not p.exists():
        p.mkdir()
    p.rmdir()
    print("Removing {}".format(p))
    """
Removing test_for_rm
    """


def pathlib_unlink():
    """使用unlink，如果是个文件或者链接，则会删除，如果是个目录，则会调用rmdir()删除该目录"""
    p = pathlib.Path("touched")
    p.touch()
    print("exists before removing: ", p.exists())

    # 如果文件不存在，则会报：FileNotFoundError
    # 用户必须具有文件、链接、套接字等文件系统对象的删除权限
    p.unlink()
    print("exists after removing: ", p.exists())
    """
exists before removing:  True
exists after removing:  False
    """


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

    # 检测文件类型
    print("\npathlib_types: ")
    # pathlib_types()

    # 文件属性
    print("\npathlib_stat: ")
    pathlib_stat()

    print("\npathlib_ownership: ")
    # pathlib_ownership()

    print("\npathlib_touch: ")
    pathlib_touch()

    # 权限?????
    print("\npathlib_chmod: ")
    pathlib_chmod()

    # 删除
    print("\npathlib_rmdir: ")
    pathlib_rmdir()

    print("\npathlib_unlink: ")
    pathlib_unlink()
