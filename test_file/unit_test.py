import re


def is_equal_string(s1, s2):
    if (s1 is None) and (s1 is None):
        return True
    if (s1 is None) or (s2 is None):
        return False
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if (s1[i] == "*") or (s2[i] == "*"):
            continue
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == "__main__":
    a = "企业名称: 浙江大学投资控股有限公司; 出资额: ****; 百分比: ***%; 法人性质: 企业法人"
    b = "企业名称: 浙江大学投资控股有限公司; 出资额: 7000; 百分比: 100%; 法人性质: 企业法人"
    print(is_equal_string(a, b))

