import enum
import inspect


class BugStatus(enum.Enum):
    first = 1
    second = 2
    third = 3
    fourth = 4


# IntEnum支持整数比较
class SortEnum(enum.IntEnum):
    a = 1
    b = 2
    c = 3
    d = 4

    # 如果出现相同的值，则后出现的相当于是第一次出现的变量的别名
    # SortEnum.b is SortEnum.k返回的是True
    k = 2
    g = 3


# 创建具有唯一值的枚举类, 如果有相同值的类成员会报错。
# @enum.unique
# class UnionEnum(enum.Enum):
#     a = 1
#     b = 2
#     c = 3
#
#     d = 1

class ThirdEnum(enum.Enum):
    new = (3, ["f", "s", "t"])
    f = (4, ["5", "6"])
    s = (5, ["7", "8"])
    t = (6, ["9", "10"])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transitions(self, new_state):
        return new_state.name in self.transitions


if __name__ == "__main__":
    for name, value in inspect.getmembers(enum):
        if name.startswith("_"):
            continue
        print("%s=%r" % (name, value))

    b = BugStatus
    print(b.first.name, b.first.value)
    print(b.second.name, b.second.value)

    for status in BugStatus:
        print("{:<15} = {}".format(status.name, status.value))

    a = BugStatus.first
    b = BugStatus.second
    print(a == b)
    print(a is b)
    try:
        print(a > b)
        print(a < b)
    except TypeError as err:
        print("key error")

    # 支持比较的enum类
    print([s.name for s in sorted(SortEnum)])

    for s in SortEnum:
        print(s.name, ": ", s.value)
    print(SortEnum.b is SortEnum.k)
    print(SortEnum.b.name is SortEnum.k.name)

    # print([s.name for s in UnionEnum])
    # print(UnionEnum.a is UnionEnum.b)

    # 自增成员变量
    new_enum = enum.Enum(
        value="increase_enum",
        names=("here that this match"),
    )
    for s in new_enum:
        print(s.name, ": ", s.value)

    second_enum = enum.Enum(
        value="second",
        names=[
            ("a", 1),
            ("b", 2),
            ("c", 3),
        ],
    )
    for s in second_enum:
        print(s.name, ": ", s.value)

    for s in ThirdEnum:
        print(s.name, ": ", s.value)

    print("new name: ", ThirdEnum.new.name)
    print("new value: ", ThirdEnum.new.value)
    print("transitions: ", ThirdEnum.new.transitions)
    print(ThirdEnum.new.can_transitions(ThirdEnum.f))
