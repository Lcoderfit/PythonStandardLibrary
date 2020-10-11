import string


def template_case():
    values = {"var": 10}

    # $与{}搭配
    t = string.Template("""
    a:  $var
    b: $$
    c: ${var}ible
    """)
    print("template1: ", t.substitute(values))

    # 格式化字符串
    t = """
    a:  %(var)s
    b:  %%
    c:  %(var)sible
    """
    print("template2: ", t % values)

    # format函数
    t = """
    a:  {var}
    b:  {{}}
    c:  {var}ible
    """
    print("template3: ", t.format(**values))

    t = string.Template("$var is not a template $missing")
    try:
        print("substitute(): ", t.substitute(values))
    except KeyError as err:
        print("Error: ", err)
    print("safe_substitute(): ", t.safe_substitute(values))


class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = r'[a-z]+_[a-z]*'


if __name__ == "__main__":
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.hexdigits, string.octdigits)

    print(string.punctuation)
    if "\t" in string.whitespace:
        print("yes")

    print(string.printable, len(string.printable))

    # s = string.Formatter()
    # print(s.vformat("a, {0}, {1}", ))

    # 将所有单词的首字母转成大写
    s = "i am a little coder"
    print(string.capwords(s))
    print()

    # 模板与字符串拼接或者格式化字符串的不同点： 模板不考虑参数的类型，直接转换为字符串
    template_case()
