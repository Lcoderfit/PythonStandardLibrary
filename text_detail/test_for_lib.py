import maya
import re
import copy
import json
import tarfile
import os
import zipfile


def test_for_data(_):
    """测试用例"""
    data = list()
    # 公司名称中包含年份
    res_date = re.search(r"\d{2,4}-\d{1,2}-\d{1,2}", _["org_name"])
    if res_date:
        # 置否原始数据，然后新增一条
        new_data = copy.deepcopy(_)
        _["valid"] = 0
        data.append(_)
        _ = new_data
        # 对比年月日出现的位置和括号出现的位置
        date_pos = _["org_name"].index(res_date.group())
        left_bracket = _["org_name"].find(u"(")
        # 日期出现在括号内，则去除org_name中的括号部分; 日期在左括号左边，则判断是否有“公司”，
        # 有“公司”则截取包含公司的部分，没有则直接将日期及之后的部分去除
        if (left_bracket > -1) and (left_bracket < date_pos):
            _["org_name"] = _["org_name"][:left_bracket]
        else:
            _["org_name"] = _["org_name"][:date_pos]
            word_pos = _["org_name"].rfind(u"公司")
            if word_pos > -1:
                _["org_name"] = _["org_name"][:word_pos + 2]

    # 公司名称以"公"结尾，缺少"司"字
    if re.match(r"^.+公$", _["org_name"]):
        # 原始数据置否，新增一个数据，org_name加上"司"
        if not data:
            new_data = copy.deepcopy(_)
            _["valid"] = 0
            data.append(json.dumps(_))
            _ = new_data
        _["org_name"] = _["org_name"] + u"司"
    data.append(_)
    return data


def generate_tar_file(tar_path):
    if os.path.exists(tar_path):
        os.remove(tar_path)

    with tarfile.open(r"NiceLib.tar", "a") as t:
        t.add("NiceLib")

    with tarfile.open(r"NiceLib.tar", "r") as t:
        for m in t.getnames():
            print(m)


def make_dirs_to_zip(source_dir, zip_name):
    """将文件打包成zip压缩包"""
    print("******************zip start******************")
    with zipfile.ZipFile(zip_name, "w") as z:
        # 出去要压缩的文件的路径长度(最右边不带斜杠)
        base_path_len = len(os.path.dirname(source_dir))
        for parent, dir_names, file_names in os.walk(source_dir):
            for file_name in file_names:
                file_path = os.path.join(parent, file_name)
                # 在zip包中的归档路径（用相对路径表示）
                archive_name = file_path[base_path_len:].strip(os.path.sep)
                z.write(file_path, archive_name)
    print("******************zip end******************")


if __name__ == "__main__":
    # base_path = r"D:\PrivateProject\Python-Tags"
    # source_dir_cur = os.path.join(base_path, r"NiceLib")
    # # 最好用绝对路径，且生成zip的路径不能包含在要压缩的文件夹内部，否则会一直递归压缩，生成的zip包会越来越大
    # # 如果运行生成zip的程序在需要压缩的文件夹内，则如果不用绝对路径设置压缩路径在要压缩的文件夹外部，则会产生递归压缩
    # zip_name_cur = os.path.join(base_path, "NiceLib.zip")
    # make_dirs_to_zip(source_dir_cur, zip_name_cur)

    path = r"/home/scrapyer/workspace/luhu/"
    print(os.path.split(path))
