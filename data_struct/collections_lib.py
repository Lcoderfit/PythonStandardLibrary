import collections
import time
import threading
import random


def test_chainmap():
    a = {"p": "P1"}
    b = {"q": "Q", "p": "P2"}

    # 如果a跟b中包含相同的key，则m中这个key的值是对应在a中的值（与传入ChainMap的参数顺序有关）
    m = collections.ChainMap(a, b)
    print(m["p"])
    print(m["q"])

    print(list(m.keys()))
    print(list(m.values()))

    # 字典映射列表
    print(m.maps)
    m.maps = list(reversed(m.maps))
    print(m.maps)
    print(m["p"])

    print(m["q"])
    # 修改原来的字典的值，chainmap也会改变
    b["q"] = "change Q"
    print(m["q"])
    # 对m赋新值时，也会改变原来的字典值
    print("m的值更改前")
    print(m)
    print()
    print("m的值更改后")
    # 会影响b["q"]的值
    m["q"] = "m_change_q"
    print(b)


def test_new_child():
    a = {"p": "P", "q": "Q"}
    b = {"w": "W", "q": "Q1"}
    m1 = collections.ChainMap(a, b)
    # 改变m2，不会改变原字典，改变原字典也不会影响到m2
    m2 = m1.new_child()
    print("m1 before: ", m1)
    print("m2 before: ", m2)

    m2["p"] = "P1"
    print("m1 after: ", m1)
    print("m2 after: ", m2)


def test_by_paramss():
    a = {"p": "P", "q": "Q"}
    b = {"w": "W", "q": "Q1"}
    c = {"r": "R"}
    m1 = collections.ChainMap(a, b)
    # 等价于： m2 = m1.new_child()  m2["r"] = "R"
    m2 = m1.new_child(c)
    print(m2)

    # 或者直接如下
    m2 = collections.ChainMap(c, *m1.maps)
    print(m2)


def init_counter():
    """初始化counter"""
    # 有两个a，三个b，一个c： Counter({'b': 3, 'a': 2, 'c': 1})
    a = collections.Counter(["a", "b", "c", "a", "b", "b"])
    b = collections.Counter({"a": 2, "b": 3, "c": 1})
    c = collections.Counter(a=2, b=3, c=1)
    print("a: ", a)
    print("b", b)
    print("c", c)

    # 通过update方法填充
    a = collections.Counter()
    # 会统计出现的字符及其总个数
    a.update("abaacb")
    print("通过update方法填充： ", a)
    # 传入的字典中的key，必须出现在原来的a中，且Counter是进行数字的叠加（如果a原来的值为3，则出入{"a": 1}之后a的值变为4（3+1））
    a.update({"a": 1, "c": 5})
    print("传入字典到update方法中: ", a)


def count_chars():
    c = collections.Counter("ababcad")
    # Counter中没有的字符，则计数值为0
    for letter in "abced":
        print("{} : {}".format(letter, c[letter]))

    # 返回Counter中的所有元素, elements()返回的是一个迭代器
    print("elements: ", [e for e in c.elements()])
    # 获取不存在的字符，不会报错，会返回一个0值
    print(c["k"])


def collections_counter_most_common():
    c = collections.Counter()
    with open("a.txt", "r") as f:
        for line in f.readlines():
            c.update(line.rstrip().lower())

    print("common chars: ")
    # 打印三个出现次数最多的字母
    for letter, count in c.most_common(3):
        print(letter, ": ", count)


def collections_counter_arithmetic():
    c1 = collections.Counter(["a", "b", "c", "a", "b", "b"])
    c2 = collections.Counter("alphabet")
    print("C1: ", c1)
    print("C2: ", c2)

    # 合并，相同的key会相加
    print("combined counts: ")
    print(c1 + c2)

    # 差集
    print("Subtraction: ")
    print(c1 - c2)

    # 交集, 相同的key值会相减，操作后结果为0或负数的key会被删除
    print("Intersection: ")
    print(c1 & c2)

    # 并集
    print("Union")
    print(c1 | c2)


def collections_default_dict():
    def default_factory():
        return "default value"
    # 如果所有键都有相同的默认值，且默认值为容器类型，则非常有用
    d = collections.defaultdict(default_factory, foo="bar")
    print("foo: ", d["foo"])
    print("k2: ", d["k2"])


def collections_deque():
    """双端队列"""
    d = collections.deque("abcdefg")
    print("Deque: ", d)
    print("Length: ", len(d))
    print("Left end: ", d[0])
    print("Right end: ", d[-1])

    # 删除元素
    d.remove("c")
    print("remove(c): ", d)


def collections_population():
    d1 = collections.deque()
    # 从右边填充
    d1.extend("abcdef")
    print("extend: ", d1)
    d1.append("9")
    print("append: ", d1)

    # 从左边填充
    d2 = collections.deque()
    # deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    d2.extendleft(range(10))
    print("extendleft: ", d2)
    d2.appendleft("9")
    print("appendleft: ", d2)


def collections_consuming():
    d = collections.deque("abcdefg")
    while True:
        try:
            # 从右边删除
            print(d.pop(), end="")
        except IndexError:
            break
    print()

    # 从左边删除
    # 5 4 3 2 1 0
    d = collections.deque(range(6))
    while True:
        try:
            print(d.popleft(), end="")
        except IndexError:
            break
    print()


# 双端队列是线程安全的
def collections_deque_both_ends():
    candle = collections.deque(range(5))

    def burn(direction, next_source):
        while True:
            try:
                n = next_source()
            except IndexError:
                break
            else:
                print("{:>8}: {}".format(direction, n))
                time.sleep(0.1)

        print("{:>8} done".format(direction))
        print()

    left = threading.Thread(target=burn, args=('Left', candle.popleft))
    right = threading.Thread(target=burn, args=('Right', candle.pop))

    left.start()
    right.start()

    left.join()
    left.join()


def collections_deque_rotate():
    d = collections.deque(range(10))
    print("Normal: ", d)

    # 取最右边的两个元素，放到左边
    d.rotate(2)
    print("Right Rotate: ", d)
    # 取最左边的元素，放到最右边
    d = collections.deque(range(10))
    d.rotate(-2)
    print("Left Rotate: ", d)


def collections_deque_maxlen():
    random.seed(1)
    # 当长度超过限制后，会删除老的元素
    d1 = collections.deque(maxlen=3)
    d2 = collections.deque(maxlen=3)
    for i in range(5):
        n = random.randint(0, 100)
        print('n=', n)
        d1.append(n)
        d2.appendleft(n)
        print("D1: ", d1)
        print("D2: ", d2)


if __name__ == "__main__":
    # Q: ChainMap的主要作用是什么？？
    test_chainmap()
    test_new_child()
    print()
    test_by_paramss()

    # Counter
    print()
    init_counter()
    count_chars()
    print()
    collections_counter_most_common()

    print()
    collections_counter_arithmetic()

    print()
    collections_default_dict()
    print()
    collections_deque()
    print()
    collections_population()
    print()
    collections_consuming()
    print()
    collections_deque_both_ends()
    print()
    collections_deque_rotate()
    print()
    collections_deque_maxlen()
