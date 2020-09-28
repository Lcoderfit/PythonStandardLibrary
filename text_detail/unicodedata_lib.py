import unicodedata


if __name__ == "__main__":
    s = "hello world, Lcoderfit"
    print(unicodedata.lookup('left curly bracket'))

    print(unicodedata.name('\\'))
    print(unicodedata.decimal("1"))
    print(unicodedata.digit("4"))
    print(unicodedata.numeric("9"))
    print(unicodedata.category("/"))

    print(unicodedata.bidirectional("b"))

    print(unicodedata.east_asian_width("b"))
    print(unicodedata.mirrored("{}"))