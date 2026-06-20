"""
33. 搜索旋转排序数组
题目与链接见同文件夹 problem.md，知识点见 notes.md。
分类通用模板见 ../binary_search.py。

思路 (三句话):
  1. 本质是"在被旋转过、不整体有序的数组里找 target"，且要求 O(log n)，不能扫一遍。
  2. 关键洞见：砍一刀取 mid 后，[left..mid] 和 [mid..right] 里【至少有一半是完整升序】的。
     先用 nums[left] <= nums[mid] 判断哪半边升序；在那个升序半边里用普通二分判断
     target 在不在，决定往哪边缩。
  3. 时间 O(log n)，空间 O(1)。一次二分搞定。

掌握度: 🔴 (第一次做)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:          # 左半段 [left..mid] 升序
                # TODO: target 落在左半段升序区间 [nums[left], nums[mid]) 里吗？
                #   条件: nums[left] <= target < nums[mid]
                #     是  -> 往左缩 right = mid - 1
                #     否  -> 往右缩 left  = mid + 1
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                                 # 右半段 [mid..right] 升序
                # TODO: target 落在右半段升序区间 (nums[mid], nums[right]] 里吗？
                #   条件: nums[mid] < target <= nums[right]
                #     是  -> 往右缩 left  = mid + 1
                #     否  -> 往左缩 right = mid - 1
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))   # 期望: 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))   # 期望: -1
    print(s.search([4, 5, 6, 7, 0, 1, 2], 6))   # 期望: 2
    print(s.search([6, 7, 0, 1, 2, 4, 5], 5))   # 期望: 6  (触发"右半段升序"分支)
    print(s.search([1], 0))                      # 期望: -1
    print(s.search([1], 1))                      # 期望: 0
