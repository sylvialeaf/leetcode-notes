"""
704. 二分查找 / Binary Search
题目与链接见同文件夹 problem.md，知识点见 notes.md。

思路 (面试就讲这三句):
  1. 本质是"在有序数组里找一个数"。
  2. 二分查找：每次看中间 mid，比较 nums[mid] 和 target，砍掉不可能的那一半，
     移动 left / right 缩小范围。关键：利用"有序"，每次范围减半。
  3. 时间 O(log n) 空间 O(1)，因为每比较一次范围就减半。

掌握度: 🔴 (待你填代码)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 【第1件事】两个指针圈出查找范围：一开始是整个数组
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

        # 循环结束还没找到，说明不在
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    print(s.search(nums, 9))   # 期望: 4
    print(s.search(nums, 2))   # 期望: -1
    print(s.search(nums, -1))  # 期望: 0
    print(s.search(nums, 12))  # 期望: 5
