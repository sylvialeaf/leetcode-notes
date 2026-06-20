"""
875. 爱吃香蕉的珂珂  —— 二分答案 的入门题
题目与链接见同文件夹 problem.md，知识点见 notes.md。
分类通用模板见 ../binary_search.py。

思路 (三句话):
  1. 本质是"求满足条件的最小值"：速度越快越容易吃完，存在临界点(✗✗✗✓✓✓)，要找第一个✓。
  2. 二分答案：在速度范围 [1, max(piles)] 上二分；判定函数 check(k)=用速度k算总小时数<=h吗；
     找第一个让 check 成立的 k（= 153 那套 while left<right + right=mid 模板）。
  3. 时间 O(n log(max))，空间 O(1)。

★ 二分答案套路：不是在数组里找元素，而是在"答案的取值范围"上二分，配一个 check 判定函数。
  关键三件套：①答案范围 ②check(x) 判定 ③在范围上找第一个/最后一个满足的值。

掌握度: 🔴 (第一次做)
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int) -> bool:
            # 用速度 k，算吃完所有香蕉要几小时，<= h 就算成功
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)          # TODO: 这堆要几小时，向上取整 -> math.ceil(pile / k)
            return hours <= h

        left, right = 1, max(piles)   # 速度范围：最慢1，最快=最大堆
        while left < right:           # 同 153："缩到单个幸存者"模板
            mid = (left + right) // 2
            if check(mid):
                # mid 这个速度能吃完 -> 答案是 mid 或更小 -> 保留 mid 往左缩
                right = mid           # TODO: 填 mid（不是 mid - 1）
            else:
                # mid 太慢吃不完 -> 答案更大
                left = mid + 1            # TODO: 填 mid + 1
        return left                   # 第一个能吃完的速度 = 最小速度


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))            # 期望: 4
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))      # 期望: 30
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))      # 期望: 23
    print(s.minEatingSpeed([312884470], 968709470))      # 期望: 1  (h很大,最慢就够)
