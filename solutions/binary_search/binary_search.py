"""
二分查找 · 通用模板（套路心法）
====================================
这是「二分查找」这一类的通用模板，不是某道具体题。做这类题先回忆这里的套路。
具体题目放在本文件夹的子文件夹里（如 704_binary_search/）。

适用信号：数据【有序】，要"找某个值 / 找满足条件的边界 / 二分一个答案"。
核心心法：每次看中间，砍掉不可能的一半，范围对半减 → O(log n)。

下面三个模板按需取用：找值 / 找左边界 / 找右边界。
"""
from typing import List


# ── 模板 A：找某个值（最基础，对应 LC704）──────────────────
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1          # 闭区间 [left, right]
    while left <= right:                     # 注意带等号
        mid = left + (right - left) // 2     # 防溢出写法（Python 可直接 //2，但养成好习惯）
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:             # 中间太小 → 去右半
            left = mid + 1
        else:                                # 中间太大 → 去左半
            right = mid - 1
    return -1                                # 没找到


# ── 模板 B：找 target 第一次出现的位置（左边界，对应 LC34 前半）──
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:              # 满足条件，记录后继续往左缩
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans                               # 第一个 >= target 的下标（-1 表示没有）


# ── 模板 C：找 target 最后一次出现的位置（右边界，对应 LC34 后半）──
def upper_last(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:              # 满足条件，记录后继续往右扩
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


# 易错点：① while 带等号 left<=right ② 指针要 mid±1，别写成 mid（会死循环）
# ③ 找边界时"找到也别急着返回"，记下来继续缩，才能逼到第一个/最后一个

if __name__ == "__main__":
    a = [-1, 0, 3, 5, 9, 12]
    print(search(a, 9))        # 4
    b = [5, 7, 7, 8, 8, 10]
    print(lower_bound(b, 8))   # 3 （第一个 8 的下标）
    print(upper_last(b, 8))    # 4 （最后一个 8 的下标）
