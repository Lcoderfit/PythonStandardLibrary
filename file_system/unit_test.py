import pathlib


def test_for_unlink():
    """测试unlink方法"""
    p = pathlib.Path("testfile")
    # p.mkdir()
    # unlink好像无法删除目录，但可以删除文件跟链接
    p.unlink()


if __name__ == '__main__':
    test_for_unlink()
