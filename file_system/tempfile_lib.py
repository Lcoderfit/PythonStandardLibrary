import pathlib
import os
import tempfile


def tempfile_TemporaryFile():
    """创建临时文件系统，当用close或者with或上下文管理器关闭这个文件时，这个文件会被自动删除"""
    print("Building a filename with PID:")
    filename = "test_temp_{}.txt".format(os.getpid())
    with open(filename, "w+") as temp:
        print("temp: ")
        print("{!r}".format(temp))
        print("temp.name: ")
        print("{!r}".format(temp.name))
    os.remove(filename)

    print()
    print("TemporaryFile: ")
    with tempfile.TemporaryFile() as temp:
        print("temp:")
        print("{!r}".format(temp))
        print("temp.name: ")
        print("{!r}".format(temp.name))
    """
tempfile_TemporaryFile: 
Building a filename with PID:
temp: 
<_io.TextIOWrapper name='test_temp_5156.txt' mode='w+' encoding='cp936'>
temp.name: 
'test_temp_5156.txt'

TemporaryFile: 
temp:
<tempfile._TemporaryFileWrapper object at 0x00000000021D1DC8>
temp.name: 
'C:\\Users\\VIRUSE~1.V-D\\AppData\\Local\\Temp\\tmp2b8qi0ld'
    """


def tempfile_TemporaryFile_binary():
    """读写临时文件"""
    # 临时文件
    # 默认采用的是w+b模式创建的文件句柄
    with tempfile.TemporaryFile() as temp:
        temp.write("Lcoderfit".encode("utf8"))
        # 写完之后需要通过seek将文件句柄回转到开头
        temp.seek(0)
        print(temp.read())
    """
b'Lcoderfit'
    """


def tempfile_TemporaryFile_text():
    """以文本模式打开临时文件"""
    # 模式之间需要通过“+”连接，否则会报错： io.UnsupportedOperation: not readable
    with tempfile.TemporaryFile(mode='w+t') as temp:
        temp.writelines(["love codeing\n", "and fighting\n"])
        temp.seek(0)
        for line in temp:
            print(line.rstrip())
    """
love codeing
and fighting
    """


def tempfile_NamedTemporaryFile():
    """命名文件,可以通过name属性在不同进程或者主机之间访问，文件句柄关闭后文件会被删除"""
    with tempfile.NamedTemporaryFile() as temp:
        print("temp: ")
        print('{!r}'.format(temp))
        print("temp.name: ")
        print("{!r}".format(temp.name))

        f = pathlib.Path(temp.name)
    print("Exists after close: ", f.exists())
    """
<tempfile._TemporaryFileWrapper object at 0x0000000002171E88>
temp.name: 
'C:\\Users\\VIRUSE~1.V-D\\AppData\\Local\\Temp\\tmpunwujkl6'
Exists after close:  False
    """


def tempfile_SpooledTemporaryFile():
    """当临时文件中包含数据较少时，使用SpooledTemporaryFile更高效，会读写缓冲区"""
    # max_size可以设置缓冲区大小
    with tempfile.SpooledTemporaryFile(max_size=100, mode="w+t", encoding="utf-8") as temp:
        print("temp: {!r}".format(temp))

        # 循环3次，则缓冲区中写入的字符数量超过100（在第三次循环时），所以第三次循环时缓冲区中的数据会滚动到磁盘
        for i in range(3):
            temp.write("This line is repeated over and over.\n")
            print(temp._rolled, temp._file)
    """
tempfile_SpooledTemporaryFile: 
temp: <tempfile.SpooledTemporaryFile object at 0x00000000021B3608>
False <_io.StringIO object at 0x000000000290F678>
False <_io.StringIO object at 0x000000000290F678>
True <tempfile._TemporaryFileWrapper object at 0x00000000021B3C88>
    """


def tempfile_SpooleTemporaryFile_explicit():
    """显示的将缓冲区数据写入磁盘"""
    with tempfile.SpooledTemporaryFile(max_size=1000, mode="w+t", encoding="utf-8") as temp:
        for i in range(3):
            temp.write("this line is repeated over and over.\n")
            print(temp._rolled, temp._file)
        print("rolling over: ")
        # 滚动到磁盘
        temp.rollover()
        print(temp._rolled, temp._file)
    """
tempfile_SpooleTemporaryFile_explicit: 
False <_io.StringIO object at 0x00000000028530D8>
False <_io.StringIO object at 0x00000000028530D8>
False <_io.StringIO object at 0x00000000028530D8>
rolling over: 
True <tempfile._TemporaryFileWrapper object at 0x00000000021B3608>
    """


def tempfile_TemporaryDirectory():
    """需要生成多个临时文件，可以先生成一个目录，然后在该目录中打开多个文件"""
    with tempfile.TemporaryDirectory() as directory_name:
        the_dir = pathlib.Path(directory_name)
        print(the_dir)
        a_file = the_dir / "a_file.txt"
        a_file.write_text("This file is deleted")
    print("Directory is exists after?: ", the_dir.exists())
    print("Contents after: ", list(the_dir.glob("*")))
    r"""
C:\Users\VIRUSE~1.V-D\AppData\Local\Temp\tmp4xrapo9n
Directory is exists after?:  False
Contents after:  []
    """


def tempfile_NamedTemporaryFile_args():
    """为临时文件添加可预测的部分"""
    # dir参数必须是存在在系统中的路径，否则会报错
    with tempfile.NamedTemporaryFile(suffix='_suffix', prefix='prefix_', dir=r".") as temp:
        print("temp: ")
        print(" ", temp)
        print('temp.name: ')
        print(" ", temp.name)
    r"""
tempfile_NamedTemporaryFile_args: 
temp: 
  <tempfile._TemporaryFileWrapper object at 0x0000000001E85948>
temp.name: 
  D:\PrivateProject\Python-Tags\PythonStandardLibrary\file_system\prefix_rbxo9zi5_suffix
    """


def tempfile_settings():
    """临时文件默认设置: 包含临时文件的目录和创建的临时文件的前缀"""
    print("gettempdir(): ", tempfile.gettempdir())
    print("gettempprofix(): ", tempfile.gettempprefix())
    r"""
gettempdir():  C:\Users\VIRUSE~1.V-D\AppData\Local\Temp
gettempprofix():  tmp
    """


def tempfile_tempdir():
    """设置临时文件存放的位置"""
    tempfile.tempdir = "."
    print(tempfile.gettempdir())
    """
tempfile_tempdir: 
.
    """


if __name__ == '__main__':
    # 用于安全的创建临时文件系统资源
    # 可以用于临时创建文件，写入内容然后读取（无需保存文件），或者直接用于联系文件操作，省得创建的文件又要删除
    print("\ntempfile_TemporaryFile: ")
    tempfile_TemporaryFile()

    print("\ntempfile_TemporaryFile_binary: ")
    tempfile_TemporaryFile_binary()

    print("\ntempfile_TemporaryFile_text: ")
    tempfile_TemporaryFile_text()

    print("\ntempfile_NamedTemporaryFile; ")
    tempfile_NamedTemporaryFile()

    print("\ntempfile_SpooledTemporaryFile: ")
    tempfile_SpooledTemporaryFile()

    print("\ntempfile_SpooleTemporaryFile_explicit: ")
    tempfile_SpooleTemporaryFile_explicit()

    print("\ntempfile_TemporaryDirectory: ")
    tempfile_TemporaryDirectory()

    print("\ntempfile_NamedTemporaryFile_args: ")
    tempfile_NamedTemporaryFile_args()

    print("\ntempfile_settings: ")
    tempfile_settings()

    print("\ntempfile_tempdir: ")
    tempfile_tempdir()
