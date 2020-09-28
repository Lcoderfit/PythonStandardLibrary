import maya
import re
import copy
import json


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


if __name__ == "__main__":
    org_name = None
    if org_name and ((len(org_name) > 50 and org_name[-2:] != u"公司") or (org_name.find(u"&times;") > -1)):
        return data
