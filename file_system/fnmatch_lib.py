import fnmatch
import os
import pprint


def fnmatch_fnmatch():
    """判断文件是否匹配"""
    pattern = "*.PY"
    print("Pattern: ", pattern)
    print()
    files = os.listdir(".")
    for name in files:
        print("Filename: {:<25} {}".format(name, fnmatch.fnmatch(name, pattern)))
    """
Pattern:  *.py

Filename: a                         False
Filename: dir                       False
Filename: fnmatch_lib.py            True
Filename: global_lib.py             True
Filename: os_lib.py                 True
Filename: pathlib_lib.py            True
Filename: testfile                  False
Filename: test_file                 False
Filename: test_for_chmod.txt        False
Filename: test_for_rglobal          False
Filename: unit_test.py              True
    """


def fnmatch_fnmatchcase():
    """区分大小写的匹配"""
    pattern = "*.PY"
    files = os.listdir(".")
    for name in files:
        print("Filename: {:<25}  {}".format(name, fnmatch.fnmatchcase(name, pattern)))
    """
Filename: a                          False
Filename: dir                        False
Filename: fnmatch_lib.py             False
Filename: global_lib.py              False
Filename: os_lib.py                  False
Filename: pathlib_lib.py             False
Filename: testfile                   False
Filename: test_file                  False
Filename: test_for_chmod.txt         False
Filename: test_for_rglobal           False
Filename: unit_test.py               False
    """


def fnmatch_filter():
    """返回匹配的文件名序列"""
    pattern = "*.py"
    print("Pattern: ", pattern)

    files = os.listdir(".")
    print("Files: ")
    # pprint会将list中的元素一行一个打印出来
    pprint.pprint(files)

    print("Matches: ")
    # 第一个参数需要示一个列表
    pprint.pprint(fnmatch.filter(files, pattern))
    """
Pattern:  *.py
Files: 
['a',
 'dir',
 'fnmatch_lib.py',
 'global_lib.py',
 'os_lib.py',
 'pathlib_lib.py',
 'testfile',
 'test_file',
 'test_for_chmod.txt',
 'test_for_rglobal',
 'unit_test.py']
Matches: 
['fnmatch_lib.py',
 'global_lib.py',
 'os_lib.py',
 'pathlib_lib.py',
 'unit_test.py']
    """


def fnmatch_translate():
    """将glob模式转换为一个正则表达式"""
    pattern = "*.py"
    regex = fnmatch.translate(pattern)
    print("glob pattern: ", pattern)
    print("regexp pattern: ", regex)


if __name__ == '__main__':
    # 判断文件是否匹配
    print("\nfnmatch_fnmatch: ")
    fnmatch_fnmatch()

    print("\nfnmatch_fnmatchcase: ")
    fnmatch_fnmatchcase()

    print("\nfnmatch_filter: ")
    fnmatch_filter()

    print("\nfnmatch_translate: ")
    fnmatch_translate()
