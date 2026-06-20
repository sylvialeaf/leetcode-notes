"""
34. 在排序数组中查找元素的第一个和最后一个位置
题目与链接见同文件夹 problem.md，知识点见 notes.md。
分类通用模板见 ../binary_search.py（模板 B 找左边界 / 模板 C 找右边界）。

思路 (三句话):
  1. 本质是"在有序数组里找 target 的左右边界"。
  2. 做两次二分：找第一个(命中后往左压 right=mid-1) + 找最后一个(命中后往右压 left=mid+1)。
     关键：命中时不立刻返回，记下 ans=mid 继续往一边找。
  3. 时间 O(log n) 空间 O(1)。

掌握度: 🟡 (find_last 镜像独立推出，ans=mid 经点拨)
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 这层是"管道"，已经帮你写好：分别找第一个和最后一个位置
        first = self.find_first(nums, target)
        if first == -1:                 # 第一个都找不到 -> 整个不存在
            return [-1, -1]
        last = self.find_last(nums, target)
        return [first, last]

    def find_first(self, nums: List[int], target: int) -> int:
        # 找 target【第一次】出现的下标，不存在返回 -1。
        # 还是二分！但难点：当 nums[mid] == target 时，它不一定是"第一个"，
        #   它左边可能还有 target。所以——先把 mid 记下来(ans=mid)，
        #   然后该往哪半边继续找更靠前的 target？(left 动还是 right 动?)
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            # TODO: 三种情况
            #   nums[mid] == target -> 记下 ans=mid，继续往___找
            #   nums[mid] <  target -> left = mid + 1
            #   nums[mid] >  target -> right = mid - 1
            if  nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] <  target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def find_last(self, nums: List[int], target: int) -> int:
        # 找 target【最后一次】出现的下标，不存在返回 -1。
        # 和 find_first 镜像：命中时记下 ans，往【另一边】继续找更靠后的 target。
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            # TODO: 三种情况（和 find_first 只差命中时往哪边走）
            if  nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] <  target:
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))  # 期望: [3, 4]
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))  # 期望: [-1, -1]
    print(s.searchRange([], 0))                    # 期望: [-1, -1]
    print(s.searchRange([1], 1))                    # 期望: [0, 0]
