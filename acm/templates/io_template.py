"""
ACM 模式输入输出模板（Python）—— 笔试常用，背熟这几套就够

力扣 = 核心代码模式：只写函数，输入输出框架帮你处理。
笔试  = ACM 模式：你要自己读 stdin、打印 stdout。算法不变，区别只在"读"和"写"。

核心三件套：
  - 读单行整数:    a, b = map(int, input().split())
  - 读单行数组:    nums = list(map(int, input().split()))
  - 读多行/不定行:  for line in sys.stdin: ...
"""
import sys


# ── 1. 单行：两个整数 a b ──────────────────────────────
def demo_two_ints():
    a, b = map(int, input().split())
    print(a + b)


# ── 2. 单行：一串整数变数组 ────────────────────────────
def demo_int_array():
    nums = list(map(int, input().split()))
    print(sum(nums))


# ── 3. 多组数据：第一行 n，接下来 n 行 ─────────────────
def demo_n_lines():
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        print(max(nums))


# ── 4. 不定行，一直读到 EOF（最常见的坑）──────────────
def demo_until_eof():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        nums = list(map(int, line.split()))
        print(sum(nums))


# ── 5. 大数据量加速：一次性读入 + 缓冲输出 ─────────────
def demo_fast_io():
    data = sys.stdin.buffer.read().split()   # 全部 token，按空白切
    idx = 0
    n = int(data[idx]); idx += 1
    out = []
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        out.append(str(a + b))
    sys.stdout.write("\n".join(out) + "\n")   # 一次性输出，别在循环里 print


# ── 6. 读字符串 / 矩阵 ─────────────────────────────────
def demo_grid():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]        # n 行字符串
    print(len(grid), len(grid[0]) if grid else 0)


if __name__ == "__main__":
    # 想测哪个就调哪个；先从 demo_two_ints 开始熟悉
    demo_two_ints()
