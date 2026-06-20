"""
ACM 模式练手题: A + B（多组输入直到 EOF）
输入: 每行两个整数 a b ；读到文件结束
输出: 每行输出 a + b

练这题的目的不是算法，而是把"读输入"练成肌肉记忆。
本地测试：在终端运行 python a_plus_b.py，手敲几行如
  1 2
  3 4
然后按 Ctrl+Z 回车 (Windows) / Ctrl+D (Mac/Linux) 触发 EOF。
"""
import sys


def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        out.append(str(a + b))
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    main()
