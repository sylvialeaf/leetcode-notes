# 34 在排序数组中查找元素的第一个和最后一个位置 · 知识点笔记

> 按知识点梳理，配合同文件夹 `solution.py` / `problem.md`，以及分类通用模板 `../binary_search.py`（模板 B 找左边界 / 模板 C 找右边界）看。

## 1. 读题
- 题意大白话：升序数组（**可能有重复**），找 target **第一次**和**最后一次**出现的下标；不存在返回 `[-1, -1]`。
- 例子 `nums=[5,7,7,8,8,10]`：`target=8` → `[3,4]`；`target=6` → `[-1,-1]`；`nums=[]` → `[-1,-1]`。

## 2. 讲思路（面试就这么讲）
**三句话**：
1. 本质是"在有序数组里找 target 的左右边界"。
2. 做**两次二分**：一次找第一个位置（左边界），一次找最后一个位置（右边界）。关键：命中时不立刻返回，记下来继续往一边压。
3. 时间 O(log n)（两次二分相加还是 log n），空间 O(1)。

**一题三讲**：
- 暴力：从左扫到第一个 target、从右扫到最后一个 target，O(n)。
- 为什么慢：没利用有序。
- 怎么优化：两次二分各 O(log n)。

## 3. ⭐ 核心：命中时"记下来 + 往一边继续压"
普通二分（704）找到任意一个就 return，但有重复时它不一定是第一个/最后一个。所以：
- **find_first（第一个）**：`nums[mid]==target` 时 `ans=mid`，然后**往左**找更早的 → `right = mid - 1`。
- **find_last（最后一个）**：`nums[mid]==target` 时 `ans=mid`，然后**往右**找更晚的 → `left = mid + 1`。
- 两者只差命中时往哪边走，是**镜像**关系。

走 find_first（target=8）：mid=2(7<8,left=3) → mid=4(命中,ans=4,right=3) → mid=3(命中,ans=3,right=2) → 停，返回 3。`ans` 被一路刷新到真正的第一个。

## 4. 程序结构（searchRange 调度）
```
searchRange:  ① first = find_first(...)
              ② if first == -1: return [-1,-1]   # 不存在就提前返回，不必再找 last
              ③ last = find_last(...)
              ④ return [first, last]
```
- 函数调用函数：`self.find_first(...)` 让总入口把活分给两个小工。
- 提前返回（卫语句）：先挡掉"不存在"，逻辑更清晰。

## 5. 解法步骤（find_first 为例）
1. `left=0, right=len-1, ans=-1`。
2. `while left<=right`：`mid=(left+right)//2`，三种情况：
   - `==target` → `ans=mid; right=mid-1`（记下，往左）
   - `<target`  → `left=mid+1`
   - `>target`  → `right=mid-1`
3. 返回 `ans`。find_last 把命中分支改成 `ans=mid; left=mid+1`。

## 6. 复杂度
- 两次独立二分：O(log n) + O(log n) = O(log n)。空间 O(1)。

## 7. 易错点
- 记的是位置：`ans = mid`，**不是** `ans = target`（mid 是下标"在哪"，target 是值"是几"）。
- find_first / find_last 只差命中时方向（左 `right=mid-1` / 右 `left=mid+1`），别写反。
- 空数组：`right = len-1 = -1`，`while 0<=-1` 不执行，直接返回 -1，天然正确。

## 8. 面试官追问 Q&A（每题必有）
- **Q：为什么不能用普通二分（找到就 return）？**
  A：数组可能有重复，普通二分找到的是"任意一个" target，不一定是第一个/最后一个。必须命中后继续往一边压，逼到边界。
- **Q：`find_last` 里 `==target` 和 `<target` 分支动作一样，能合并吗？**
  A：能。命中和"太小"都往右走，可写成 `if nums[mid] <= target: 命中时记 ans; left=mid+1`。但分开写更直观、不易错。
- **Q：还有别的写法吗？**
  A：用"找左边界 lower_bound"：`first = 第一个 >= target 的位置`，`last = (第一个 > target 的位置) - 1`。Python 里就是 `bisect_left(nums,target)` 和 `bisect_right(nums,target)-1`。本质同一套二分。
- **Q：怎么保证 target 不存在时返回 `[-1,-1]`？**
  A：find_first 找不到会返回 -1，searchRange 检测到 `first==-1` 直接返回 `[-1,-1]`。

## 9. 顺带建立的概念
- `mid` 是下标（在哪），`target` 是值（是几）——要返回位置就记 mid。
- 函数调用函数 `self.xxx()`、提前返回（卫语句）。
- 二分的"找值 / 找左边界 / 找右边界"是同一骨架，差别只在命中时怎么处理——这是二分举一反三的关键。
