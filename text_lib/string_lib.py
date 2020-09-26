import string
import inspect


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
