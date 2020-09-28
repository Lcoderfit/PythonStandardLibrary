import tarfile
import time
import os
import io


def test_is_tarfile():
    for file_name in ["a.txt", "b.tar.gz", "c.tar", "d"]:
        try:
            print("{:>15}   {}".format(file_name, tarfile.is_tarfile(file_name)))
        except IOError as err:
            print("{:>15}   {}".format(file_name, err))


def read_tarfile():
    with tarfile.open("c.tar", "r") as t:
        print(t.getnames())


def get_tar_info():
    with tarfile.open("c.tar", "r") as r:
        # 返回归档文件的tarinfo实例列表
        print(r.getmembers())
        # 根据tar压缩包中的归档文件名，获取该归档文件的TarInfo实例
        print(r.getmember("a.txt"))

        for member_info in r.getmembers():
            print(member_info.name)
            print(member_info.mtime, time.ctime(member_info.mtime), type(member_info.mtime))
            local_time = time.localtime(member_info.mtime)
            print(local_time)
            print(time.strftime("%Y-%m-%d", local_time))
            print("mode: ", member_info.mode, oct(member_info.mode))
            print("size: ", member_info.size, "bytes")
            print("type: ", member_info.type)
            print()


def get_tar_info_by_name():
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            try:
                tar_info = r.getmember(file_name)
            except KeyError as err:
                print("{} {}".format(file_name, err))
            else:
                print("{}   {} Bytes".format(tar_info.name, tar_info.size))


def read_tar_file():
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            try:
                f = r.extractfile(file_name)
            except KeyError as err:
                print(file_name, ": ", err)
            else:
                print(file_name, ": ")
                print(f.read().decode("utf8"))


def write_file_to_file_system(dir_path):
    if os.path.exists(dir_path):
        for file_name in os.listdir(dir_path):
            os.remove(os.path.join(dir_path, file_name))
        os.rmdir(dir_path)
    os.mkdir(dir_path)
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            # 将文件解压到特定的目录中去
            r.extract(file_name, dir_path)
        print(os.listdir(dir_path))


def write_file_by_extractall(dir_path):
    if os.path.exists(dir_path):
        for file_name in os.listdir(dir_path):
            os.remove(os.path.join(dir_path, file_name))
        os.rmdir(dir_path)
    os.mkdir(dir_path)
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            # 第一个参数是写入的目录，第二个参数是TarInfo实例
            r.extractall(dir_path, members=[r.getmember(file_name)])
    print(os.listdir(dir_path))


def create_new_archive():
    # 跟文件操作一样，w是覆盖写入，a是追加新文件
    with tarfile.open("new.tar", "w") as out:
        print("Add a.txt")
        # 需要是在系统中存在的文件
        out.add("a.txt")

    print("file_list: ")
    with tarfile.open("new.tar", "r") as r:
        print(r.getnames())


def create_new_by_arcname():
    # 跟文件操作一样，w是覆盖写入，a是追加新文件
    with tarfile.open("re_new.tar", "w") as out:
        # 需要是在系统中存在的文件
        # 将__init__.py文件取一个别名压入tar压缩包中
        info = out.gettarinfo("__init__.py", arcname="t.txt")
        out.addfile(info)

    with tarfile.open("re_new.tar", "r") as r:
        print(r.getnames())


def write_tar_with_cache_string():
    text = "this is string content in cache"
    data = text.encode("utf8")

    with tarfile.open("cache.tar", "w") as out:
        # 构造一个TarInfo对象, 参数设置的是该TarInfo对应的name属性
        info = tarfile.TarInfo("cache.md")
        info.size = len(data)
        # 将内存中的数据不写入文件直接添加到归档
        out.addfile(info, io.BytesIO(data))

    with tarfile.open("cache.tar", "r") as r:
        for member in r.getmembers():
            print(member.name)
            # 根据TarInfo提取出文件对象
            f = r.extractfile(member)
            print(f.read().decode("utf8"))


def add_file_to_tar():
    with tarfile.open("new.tar", "r") as t:
        print([info.name for info in t.getmembers()])

    # with tarfile.open("new.tar", "a") as out:
    #     info = out.gettarinfo("a.txt", arcname="a.txt")
    #     out.addfile(info)
    with tarfile.open("new.tar", "a") as out:
        # 需要是在系统中存在的文件
        out.add("a.txt")

    # 注意，是t.getmembers(), 如果写成了t.members(),则只会返回tar归档里面的第一个文件名.
    with tarfile.open("new.tar", "r") as t:
        print([info.name for info in t.getmembers()])


def read_diff_format():
    fmt = "{:<30} {:<10}"
    print(fmt.format("FILENAME", "SIZE"))
    print(fmt.format("a.txt", os.stat("a.txt").st_size))
    tar_and_file_list = [
        ("o.tar", "w"),
        ("p.tar.gz", "w:gz"),
        ("q.tar.bz2", "w:bz2")
    ]
    for tar_name, write_mode in tar_and_file_list:
        with tarfile.open(tar_name, write_mode) as t:
            t.add("a.txt")

        # print(fmt.format(tar_name, os.stat(tar_name).st_size / 1024), "KB")
        print(fmt.format(tar_name, os.stat(tar_name).st_size), "B")
        print([m.name for m in tarfile.open(tar_name, "r:*").getmembers()])


if __name__ == "__main__":
    test_is_tarfile()
    read_tarfile()
    get_tar_info()
    get_tar_info_by_name()
    print()
    read_tar_file()
    print()
    dir_name = "here"
    write_file_to_file_system(dir_name)
    print()
    that_name = "that"
    write_file_by_extractall(that_name)
    print()
    create_new_archive()
    print()
    create_new_by_arcname()
    print()
    write_tar_with_cache_string()
    print()
    add_file_to_tar()
    print()
    read_diff_format()
