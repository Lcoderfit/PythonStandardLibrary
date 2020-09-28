import tarfile
import time
import os


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
            os.remove(dir_path + file_name)
        os.rmdir(dir_path)
    os.mkdir(dir_path)
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            # 将文件解压到特定的目录中去
            r.extract(file_name, dir_path)
        print(os.listdir(dir_path))


def write_file_by_extractall(dir_path):
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
    os.mkdir(dir_path)
    with tarfile.open("c.tar", "r") as r:
        for file_name in r.getnames():
            # 第一个参数是写入的目录，第二个参数是TarInfo实例
            r.extractall(dir_path, members=[r.getmember(file_name)])
    print(os.listdir(dir_path))


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
