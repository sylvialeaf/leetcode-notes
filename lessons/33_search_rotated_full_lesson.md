# 33 搜索旋转排序数组 · 带教全记录（full lesson）

> 完整保留带教对话。精炼速查版见 `solutions/binary_search/33_search_rotated/notes.md`。
> 日期：2026-06-12　难度：中等 ⭐　结果：🟡

---

## ① 读题
LeetCode 33 👉 https://leetcode.cn/problems/search-in-rotated-sorted-array/
- 大白话：原本升序的数组被从某点"掰断、前后两半对调"（旋转）。在旋转后的数组里找 target 下标，找不到返回 -1。硬约束 O(log n)（不准扫一遍）。
- 例 `[4,5,6,7,0,1,2]`（原 `[0,1,2,4,5,6,7]` 在 4/5 间掰断）：target=0→4；target=3→-1。
- 画面：两段各自升序，中间一个"断崖"（7 直接掉到 0）。

## ② 讲思路（我先抛关键直觉）

### 你的第一反应：「我想先找最大值？可以用 max() 吗？」
**点评 + 纠正**：方向对（断崖/最大值位置是破题关键），但 `max()` 是 O(n)（要挨个看一遍），**违反 O(log n)，这题就算没做对**。这正是这题的坑——逼你连找断点都用二分。

### 我抛的关键直觉问题
砍一刀取 mid 后，mid 左右两半**至少有一半是完整升序**的。
- 用 `nums[left] <= nums[mid]` 判断左半段是不是升序。
- 我问：**如果 `nums[left] > nums[mid]`，断崖在左半还是右半？**

**你的回答**：「在左边」✅ 完全正确 → 那么右半段 `[mid..right]` 反而是完整升序的。

## ③ 你卡住的点 + 怎么讲通的

### 卡点：指针移动写乱了（你的原话）
> "如果target比mid的数大，left=mid，如果left＜right，继续正常二分。反之，right=mid，此时left应该大于right，target小于mid了，left=mid..."

**纠正两点**：
1. **致命点：指针只能 `mid+1`/`mid-1`，不能光秃秃 `=mid`**。mid 已比较过、要排除；写 `=mid` 区间缩不动会死循环。你那句"left 应该大于 right…"的纠结，根源就是漏了 ±1。
2. **条件不能只比 mid**：要把 target **夹在升序区间里**（`nums[mid] < target <= nums[right]`），否则 target 比整段还大时会判错边。

### 决策树（我给，存进 notes）
```
mid==target? → return mid
否则 nums[left]<=nums[mid]?（左半升序）
   是 → nums[left]<=target<nums[mid]? 是→right=mid-1 否→left=mid+1
   否（右半升序）→ nums[mid]<target<=nums[right]? 是→left=mid+1 否→right=mid-1
```
一句话：先认出哪半边升序 → 在升序半边判 target 是否夹在区间 → 在就缩到那半边，不在去另一半。
（我还用 4 个具体例子 target=0/3/6 + 右半升序的 `[6,7,0,1,2,4,5],target=5` 走查了一遍，建立画面感。）

## ④ 写代码
你填两个内层 if 条件，都用了 Python 连续比较 `nums[left] <= target < nums[mid]`，写得很地道。

## ⑤ 自测结果
期望 `4/-1/2/6/-1/0`（6 行）→ 一次过，全对 🎉。第 4 道二分、第 2 道中等题独立拿下。

## 顺带建立的概念
变形二分心法（不要求整体有序，只要每步能稳定排除一半就能二分）；普通二分是它的特例。
