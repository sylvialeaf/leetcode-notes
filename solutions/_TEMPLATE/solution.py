"""
<题号>. <题名>
题目与链接见同文件夹 problem.md，知识点见 notes.md。

思路 (面试就讲这三句):
  1. 本质是 ___ 问题。
  2. 用 ___ 方法，关键是 ___（数据结构 / 状态定义 / 不变量）。
  3. 时间 O(___) 空间 O(___)，因为 ___。

掌握度: 🔴 没思路 / 🟡 看思路能写 / 🟢 独立秒写   (做完去 progress/刷题记录.md 标)
"""
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: 核心代码（力扣只需要这个函数）
        ...

    def solve_v2(self, nums: List[int]) -> int:
        # 可选：第二种解法，对比复杂度
        ...


# ↓↓↓ 自构建 case：力扣核心函数外层包一层"造样例 + 调用 + 打印输出" ↓↓↓
if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 2, 9, 7]   # 1) 造样例
    res = s.solve(nums)      # 2) 调方法
    print(res)               # 3) 打印（建议注释上"期望: xx"方便自验）
