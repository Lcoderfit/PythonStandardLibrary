import difflib
from difflib import SequenceMatcher


if __name__ == "__main__":
    a = ["c", "b", "c"]
    b = ["c", "c", "b"]
    for i in difflib.context_diff(a, b, fromfile="before.py", tofile="after.py"):
        print(i)

    print(difflib.get_close_matches(
        "核心同花顺网络股份有限公司", ["公司", "核心同花顺", "核新同花顺", "核心同花顺网络公司", "核心网络股份有限公司"], 5, 0.8)
    )

    p = "lcoderfitasdf"
    q = "Fucllcoqewrald"
    s = SequenceMatcher(None, p, q)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))

