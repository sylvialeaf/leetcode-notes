"""
35. 搜索插入位置 / Search Insert Position
题目与链接见同文件夹 problem.md，知识点见 notes.md。
分类通用模板见 ../binary_search.py（模板 A 找值 / 模板 B 找左边界）。

思路 (三句话):
  1. 本质是"在有序数组里找一个数 / 它该在的位置"。
  2. 二分查找，主体和 704 一样；关键洞见：插入位置 = 比 target 小的数有几个，
     而 left 正好在数这个数，所以找不到时 return left。
  3. 时间 O(log n) 空间 O(1)。

掌握度: 🟡 (主体自己写对，return left 经讲解后理解)
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # 【第2件事】范围里还有数就继续查
        while left <= right:
            mid = (left + right) // 2
            # 【第3件事】比较中间值，3 种情况：
            if nums[mid] == target:   # 正好找到 -> return mid
                return mid
            elif nums[mid] < target:  # 中间值太小 -> 往右半找 -> left = mid + 1
                left = mid + 1
            else:                     # 中间值太大 -> 往左半找 -> right = mid - 1
                right = mid - 1
        # 循环结束还没找到，插入位置 = "比 target 小的数有几个" —— 而 left 这个指针一直在数这个数，所以 return left 就是返回插入位置。
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # 期望: 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # 期望: 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # 期望: 4
    print(s.searchInsert([1, 3, 5, 6], 0))  # 期望: 0
