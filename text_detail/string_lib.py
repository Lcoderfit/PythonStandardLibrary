import string
import inspect


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
    delimiter = "l"
    idpattern = r"\d+"


class HisTemplate(string.Template):
    delimiter = "{{"
    idpattern = r"[_a-z0-9]*"


class HerTemplate(string.Template):
    delimiter = "{{"
    # 必须分别提供named和braced模式（变量名和带括号的变量名）
    pattern = r"""
    \{\{(?:
      (?P<escaped>\{\{) |   # Escape sequence of two delimiters
      (?P<named>[_a-z0-9]*)\}\}     |   # delimiter and a Python identifier
      <(?P<braced>[_a-z0-9]*)>  |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    """


def is_str(value):
    if isinstance(value, str):
        return True
    return False


def print_attribute():
    for name, value in inspect.getmembers(string, is_str):
        # 跳过内置属性或方法
        if name.startswith("_"):
            continue
        # print(name, "=", value)
        print("%s=%r" % (name, value))


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
    
        s = """
    a:  l123
    b:  l345
    c:  l12asdf
    d:  llcoder
    """
    d = {
        "123": "here",
        "345": "that",
        "12": "there"
    }
    t = MyTemplate(s)
    print(t.safe_substitute(d))

    s = """
    {{{{
    {{var
    """
    h = HisTemplate(s)
    print(h.safe_substitute(var="lcoderfit"))
    # 输出模板字符串的正则匹配模式（转义定界符，变量名，带括号的变量名，不合法的定界模式）
    print(h.pattern.pattern)

    s = """
    {{{{
    {{<var>}}
    """
    her = HerTemplate(s)
    print(her.safe_substitute(var="lcoder"))

    print_attribute()
