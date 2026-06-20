# 34 在排序数组中查找元素的第一个和最后一个位置 · 带教全记录（full lesson）

> 完整保留带教对话。精炼速查版见 `solutions/binary_search/34_find_first_and_last/notes.md`。
> 日期：2026-06-09　难度：中等 ⭐　结果：🟡（find_last 镜像独立推出，ans=mid 经点拨）

---

## ① 读题
LeetCode 34 👉 https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
- 大白话：升序但**可能有重复**。返回 target **第一次**和**最后一次**出现的下标；不存在返回 `[-1,-1]`。
- 例 `nums=[5,7,7,8,8,10], target=8` → `[3,4]`；`target=6` → `[-1,-1]`。

## ② 讲思路（核心难点：普通二分命中就 return，但这里要"第一个"）
**我的关键问题**：当 `nums[mid]==target` 命中时，mid 不一定是"第一个"（它左边可能还有 target）。所以**先记 `ans=mid`，然后为了找更靠前的，该动 left 还是 right？往哪半边搜？**

## ③ 你卡住的点 + 怎么讲通的

### 卡点1：「我想让 left 和 right 都=mid，各自前后移动？感觉不对」
纠正误区：**每个分支只动一个指针**，不会 left/right 同时各动。一次只走一边。
讲通：更靠前的 target 只可能在 mid **左边**（右边下标更大更靠后）→ 命中时 `ans=mid` 后 `right = mid - 1`（left 不动），"先存着这个 8，再往左看有没有更早的"。
- 走查 `find_first, target=8`：命中下标4→ans=4,right=3；命中下标3→ans=3,right=2；left>right停 → 返回 ans=3 ✅
- 小发现：命中和"太大"动作一样（都 right=mid-1），命中只多记一笔 ans → 这就是"找左边界"套路。

### 卡点2：「这是不是有嵌套？」
讲清三种"嵌套"别混：
- **循环嵌套** = while 里又有 while（这题没有）。
- **代码块嵌套** = if 写在 while 里（这题有，靠缩进，正常）。
- **函数调用** = searchRange 调 find_first（这题有，不是循环嵌套）。
- 两次二分 = O(log n)+O(log n) = O(log n)，不是循环套循环。

### 卡点3：你写出的 find_first 有个 bug —— `ans = target`
你贴了 25-45 行，思路几乎全对（最难的"命中记下来+往左 right=mid-1"抓对了），但写成 `ans = target`。
- 纠正：要返回的是**位置**，`mid` 是下标（在哪），`target` 是值（是几）。`ans=target` 会返回 8（值）而不是 3（位置）。改成 `ans = mid`。
> 一句话记牢：**mid 是下标，target 是值；要返回"在哪"就记 mid。**

### 卡点4：「17-23 行的函数是干什么的？」（searchRange）
`searchRange` 是**总入口/调度**，自己不做二分，把活分给 find_first/find_last 再组装：
```python
def searchRange(self, nums, target):
    first = self.find_first(nums, target)   # 找第一个
    if first == -1: return [-1, -1]         # 提前返回(卫语句)：第一个都没有就不用找最后一个
    last = self.find_last(nums, target)
    return [first, last]
```
顺带概念：**函数可调用函数**（`self.` = 调我自己类里的方法）；**提前返回/卫语句**先挡掉特殊情况，逻辑更清晰。

### find_last 你独立推出（镜像）
命中时一样 `ans=mid`，但找更靠后的 → `left = mid + 1`。你自己推对了——今天最难的一步。

## ④ 自测结果
期望 `[3,4] / [-1,-1] / [-1,-1] / [0,0]` → 全对 🎉。中等题独立拿下。

## 顺带建立的概念
找左/右边界套路、mid(下标) vs target(值)、函数调用函数、提前返回/卫语句、三种嵌套的区分。（均已进 cheatsheet）
