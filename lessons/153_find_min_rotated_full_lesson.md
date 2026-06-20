# 153 寻找旋转排序数组中的最小值 · 带教全记录（full lesson）

> 完整保留带教对话。精炼速查版见 `solutions/binary_search/153_find_min_rotated/notes.md`。
> 日期：2026-06-12　难度：中等　结果：🟡

---

## ① 读题
LeetCode 153 👉 https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
- 大白话：旋转过的升序数组（元素互不相同），找**整个数组里最小的数**，O(log n)（不准 min() 扫一遍）。
- 例：`[4,5,6,7,0,1,2]`→0；`[3,4,5,1,2]`→1；`[1,2,3,4,5]`→1。
- 画面：最小值 = "断崖"底部 = 旋转点。

## ② 讲思路（我给关键提示，你来推方向）
**我的提示**：这次比 `nums[mid]` 与 `nums[right]`（最小值在右段底部，和右端比最能看出断崖在哪边）。
- `nums[mid] > nums[right]` → 断崖在 mid 的 ___ 边
- `nums[mid] < nums[right]` → mid..right 升序，最小值在 mid 的 ___ 边（含 mid）

**你的回答**：「右边、左边」✅ 两个方向全对。

## ③ 这题的两个"微妙新点"（我重点讲，你之前 4 题没遇到）

### 新点1：`right = mid`，不是 `mid - 1`
第二种情况"最小值在 mid 左边、**含 mid 自己**"——mid 可能就是答案，不能排除，所以保留 → `right = mid`。
（另一支"mid 比右端大，铁定不是最小值"可排除 → `left = mid + 1`。）

### 新点2：`while left < right`，不是 `<=`
不是"命中就 return"，而是不停缩到 left、right 撞到一起、只剩一个数，那个幸存者就是最小值。
> ⚠️ 新点1、2 是一套：`right=mid`（不带-1）必须配 `while left<right`，配 `<=` 会死循环。

### 两套二分模板对比（存进 notes）
| | 704/35/34/33 找值/边界 | 153 缩到单个幸存者 |
|---|---|---|
| 循环 | `while left <= right` | `while left < right` |
| 缩边 | 两边都 mid±1 | 一边 mid+1、一边 right=mid |
| 结束 | 命中 return / 交叉 | left==right 撞上 |

## ④ 写代码 + 踩坑
你填 2 个空（`left=mid+1` / `right=mid`）。

### 踩坑：填空把占位 `___` 留着了
第一次报 `SyntaxError: invalid decimal literal`（写成 `mid + 1___`，Python 把 `1___` 当成奇怪数字）；
第二次报 `NameError: name 'mid___' is not defined`。
→ **教训：填空时把 `___` 删干净再写**。你删干净后即通过。

## ⑤ 自测结果
期望 `1/0/11/1/1`（5 行）→ 全对 🎉。最易错的 `right=mid`（不是 mid-1）你写对了。

## 顺带建立的概念
二分两套模板按"当前 mid 能不能被排除"来选；选错搭配最常见后果是死循环，所以"`=mid` 配 `<`、`mid±1` 配 `<=`"成对记。
