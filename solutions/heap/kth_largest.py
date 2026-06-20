"""
题目: 数组中的第 K 个最大元素 / Kth Largest Element in an Array   LeetCode 215
链接: https://leetcode.cn/problems/kth-largest-element-in-an-array/

思路 (面试就讲这三句):
  1. 本质是"在无序数组里求第 K 大"的 Top-K 问题。
  2. 用大小为 K 的【小顶堆】：遍历数组，堆未满就入堆，满了就和堆顶比，
     比堆顶大就替换堆顶。最后堆顶就是第 K 大。关键：小顶堆维护"当前最大的 K 个"。
  3. 时间 O(n log K) 空间 O(K)，因为每个元素最多一次 log K 的堆调整。

易错点:
  - 求第 K"大"用【小顶堆】（堆顶是 K 个里最小的，淘汰更小的）；别用大顶堆。
  - heapq 是小顶堆，正好。要大顶堆就存负数。

掌握度: 🟢 (示例题，已写好)
"""
import heapq
from typing import List


class Solution:
    # 解法一：固定大小为 K 的小顶堆（最推荐，能讲清"为什么是小顶堆"）
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # 小顶堆，最多放 K 个
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)  # 弹出最小、压入 x，一步搞定
        return heap[0]

    # 解法二：一行流（面试可提，但要说明它是 O(n + k log n)）
    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    s = Solution()
    # 1) 构建测试 case
    nums, k = [1, 3, 2, 9, 7, 10, 8, 5, 4, 11], 5
    # 2) 传参调方法
    res = s.findKthLargest(nums, k)
    res2 = s.findKthLargest_v2(nums, k)
    # 3) 处理输出
    print(res, res2)  # 期望: 7 7  (降序 11,10,9,8,7,... 第5大是7)
