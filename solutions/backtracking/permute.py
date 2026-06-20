"""
题目: 全排列 / Permutations    LeetCode 46
链接: https://leetcode.cn/problems/permutations/

思路 (面试就讲这三句):
  1. 本质是"枚举所有排列"的回溯/DFS 问题。
  2. 用回溯三步走：在每个位置【做选择】(选一个没用过的数) → 【递归】到下一位 →
     【撤销选择】(标记回未用)。关键：used 数组保证同一个数不被重复选。
  3. 时间 O(n * n!) 空间 O(n)，因为有 n! 个排列、每个长度 n。

易错点:
  - 回溯本质 = 选择 → 递归 → 撤销选择，三步缺一不可。
  - path 收集结果时要拷贝 path[:]，否则存进去的是同一个会被改的引用。

掌握度: 🟢 (示例题，已写好)
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path, used = [], [], [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])      # 拷贝！
                return
            for i, x in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True           # 做选择
                path.append(x)
                dfs()                    # 递归
                path.pop()               # 撤销选择
                used[i] = False

        dfs()
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    res = s.permute(nums)
    for row in res:
        print(row)
    # 期望 6 行: [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
