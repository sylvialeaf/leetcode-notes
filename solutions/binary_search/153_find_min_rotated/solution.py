"""
153. 寻找旋转排序数组中的最小值
题目与链接见同文件夹 problem.md，知识点见 notes.md。
分类通用模板见 ../binary_search.py。

思路 (三句话):
  1. 本质是"在旋转过的升序数组里找断崖底部（最小值/旋转点）"，要求 O(log n)，不能 min() 扫一遍。
  2. 比 nums[mid] 和 nums[right]：mid > right 说明断崖在右半(最小值在 mid 右边，排除 mid -> left=mid+1)；
     否则 mid..right 升序，最小值在 mid 左边且【可能就是 mid】-> right=mid（保留 mid）。
     不停缩到 left==right，幸存者就是最小值。
  3. 时间 O(log n)，空间 O(1)。

★ 与前 4 题不同的二分模板（"缩到单个幸存者"）：
   - while left < right（不是 <=）       —— 新点2
   - right = mid（不是 mid-1，因为 mid 可能就是答案）—— 新点1
   这两条是一套的：right=mid 必须配 while left<right，否则死循环。

掌握度: 🔴 (第一次做)
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:                     # 新点2：< 不是 <=
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 断崖在右半，最小值在 mid 右边，mid 铁定不是最小值 -> 排除它
                left = mid + 1                       # TODO: 填 mid + 1
            else:
                # mid..right 升序，最小值在 mid 左边、且 mid 可能就是答案 -> 保留 mid
                right = mid                      # TODO: 填 mid（新点1：不是 mid - 1）
        return nums[left]                        # left == right，幸存者就是最小值


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))            # 期望: 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))      # 期望: 0
    print(s.findMin([11, 13, 15, 17]))           # 期望: 11  (没旋转)
    print(s.findMin([2, 1]))                      # 期望: 1
    print(s.findMin([1]))                         # 期望: 1   (单元素)
