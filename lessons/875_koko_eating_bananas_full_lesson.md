# 875 爱吃香蕉的珂珂 · 带教全记录（full lesson）—— 二分答案入门

> 完整保留带教对话。精炼速查版见 `solutions/binary_search/875_koko_eating_bananas/notes.md`。
> 日期：2026-06-12　难度：中等 ⭐　结果：🟡

---

## ① 读题
LeetCode 875 👉 https://leetcode.cn/problems/koko-eating-bananas/
- 大白话：piles 堆香蕉，h 小时吃完。选速度 k（根/小时），**每小时挑一堆吃最多 k 根**；这堆不够 k 根就吃光、本小时剩下时间不再吃别堆。求 h 小时内吃完的**最小速度 k**。
- 例 `piles=[3,6,7,11], h=8`→k=4（耗时 1+2+2+3=8≤8）；k=3 要 10 小时 ✗。

## ② 二分答案"心法"（全新套路，我重点讲）
前 5 题在数组里找元素；这题**在"答案 k 的取值范围"上二分**，数组本身没排序。
为什么能二分？**单调性**：吃越快用时越少，存在临界点 `✗✗✗✓✓✓`，找第一个 ✓。
**三件套**：①答案范围 `[1, max(piles)]` ②判定函数 `check(k)`=用速度 k 算总小时数 ≤h ③在范围上找第一个 True（= 153 的模板二）。

### 我抛的两个确认问题 + 你的回答
- Q1：为什么右端是 `max(piles)`，再大没意义？
  **你答**：「速度比最大堆快也只能一小时吃一堆」✅
- Q2：`ceil(6/4)` 为什么是 2？
  **你答**：「6 根分 2 小时，吃不满也算一小时」✅
两个全对，心法抓得很准。

## ③ check 怎么写 + 主二分
```python
def check(k):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile / k)   # 每堆向上取整(吃不满也占整小时)
    return hours <= h
left, right = 1, max(piles)
while left < right:        # 同 153
    mid = (left + right) // 2
    if check(mid): right = mid     # 可行→保留 mid 往左缩
    else: left = mid + 1
return left
```
**向上取整两法**：`math.ceil(pile/k)`；整数技巧 `(pile+k-1)//k`（无浮点误差，面试爱考）。

## ④ 你卡住/问到的点 + 怎么讲通的

### 问1：`return hours <= h` 为什么是小于等于？
h 是最多能用的小时数，要在警卫回来前吃完。`hours==h` 刚好赶上算成功、`<h` 提前更好、`>h` 失败 → "能吃完"= 用时不超过 h，带等号因为"刚好用满 h"也允许。

### 问2：`if check(mid):` 是什么意思？
check 返回 True/False，`if check(mid):` = "调用 check(mid)，返回 True 就进 if"。等价 `if check(mid)==True:` 但 `==True` 多余。`if` 后面跟"真/假表达式"，函数返回的布尔值可直接放那。

### 问3：`math.ceil` 没见过
`math.ceil(x)` = 向上取整（天花板），`math.ceil(1.1)=2`、`math.ceil(6/4)=2`。要先 `import math`。配套 `math.floor` 向下、`//` 也是向下；要"零头也进 1"用 ceil。

### 踩坑：把 `math` 写成 `miles`
你写成 `miles.ceil(pile/k)` → `NameError: name 'miles' is not defined`（顶部 import 的是 math）。改回 math 即通过。

## ⑤ 自测结果
期望 `4/30/23/1`（4 行）→ 全对 🎉。**二分专题 6 道全部通关！**

## ⑥ 收尾延伸：复杂度怎么算（你主动问的，已归 cheatsheet）
- 时间：循环看次数（扫一遍 n、砍一半 log n）；嵌套相乘；扔常数留最高阶。
- 875 = 外层二分值域 `log m` 次 × 内层 check 每次 `O(n)` = **O(n·log m)**（m=max(piles)）。别漏 check 的 O(n)；log 是对值域取，不是数组长度。
- log n 其实是 log₂n（对半砍），但大 O 忽略常数倍，换底只差常数，所以不写底。
- 空间 O(1)：只有 hours 一个累加变量。

## 顺带建立的概念
二分答案套路（在值域上二分+check 判定，识别信号"求最小/最大的 X 使条件成立、最小化最大值"）；`if 函数()`；`math.ceil`/整数向上取整；复杂度计算方法。后续同类高频题：1011 送包裹、410 分割数组。
