import textwrap

if __name__ == "__main__":
    s = """asdfjaskdjfasdfjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk同花顺jaskdjfasdfjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
asdfjaskdjfasdfjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1823489 asjkjfkasjdfkjkjkasjdkfjaskdjfjsa jasd asjkdf asdjf
jaksdjfkajskf
    """
    # 中文算作一个字符
    for i in textwrap.wrap(s, width=10):
        print(i)

    print()
    print(textwrap.fill(s, width=100))

    print()
    a = "lcoderfit\t\b\n\t\t\t\b      hello aksdjf asjdf"
    print(textwrap.shorten(a, 30))

    p = """\t\nasdjfka
    \t\nasjdf
    """
    print(textwrap.dedent(p))

    k = """Lcoder
    
hear 
    """
    print(textwrap.indent(k, prefix="world", predicate=lambda line: line.find("hear") > -1))

    wrapper = textwrap.TextWrapper(initial_indent="*")
    print(wrapper.width)