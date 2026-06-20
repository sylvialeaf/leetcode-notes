# 易忘 API 库（Python）

> 面试前常看常新。各平台代码联想差别大，Word/白板手撕几乎无联想，所以常用 API 要背到肌肉记忆。
> 写题时一旦"卡在某个方法名/签名"上，就补到这里。

## 排序 & 自定义比较
```python
nums.sort()                                  # 原地升序
nums.sort(reverse=True)                       # 降序
arr = sorted(arr, key=lambda x: x[0])         # 按第 0 列升序
arr.sort(key=lambda x: (-x[1], x[0]))         # 先按第1列降序，再按第0列升序
import functools
arr.sort(key=functools.cmp_to_key(lambda a, b: a - b))  # 自定义比较器
```

## 堆 heapq（只有小顶堆！大顶堆存负数）
```python
import heapq
h = []
heapq.heappush(h, x)
top = heapq.heappop(h)          # 弹出最小
heapq.heapreplace(h, x)         # 先弹最小再压 x（比先 pop 再 push 快）
heapq.heapify(arr)              # O(n) 原地建堆
heapq.nlargest(k, nums)         # 前 k 大
# 大顶堆：push(-x)，取出再取负
```

## 哈希表 / 集合
```python
from collections import Counter, defaultdict
cnt = Counter(nums)             # 计数
cnt.most_common(k)              # 出现最多的 k 个 [(元素,次数),...]
d = defaultdict(list)           # 默认值 list/int/set
d.get(key, 默认值)
seen = set(); seen.add(x); x in seen
```

## 双端队列（栈/队列/滑窗）
```python
from collections import deque
q = deque()
q.append(x); q.appendleft(x)
q.pop(); q.popleft()            # 两端都 O(1)
q[0], q[-1]                     # 看两端不弹出
```

## 字符串
```python
s.split()                      # 按【任意空白】切，自动去多余空格/空串
s.split(",")                   # 按逗号切
"".join(list_of_str)           # 拼接
s.strip() / s.lstrip() / s.rstrip()
s.isdigit() / s.isalpha() / s.lower() / s.upper()
ord('a'), chr(97)              # 字符↔ASCII
```

## 数组 / 切片
```python
a = [0] * n                    # 一维
g = [[0] * m for _ in range(n)]   # 二维（别用 [[0]*m]*n，会共享引用！）
a[::-1]                        # 反转
a[i:j], a[:k], a[k:]
import bisect
bisect.bisect_left(a, x)       # x 应插入的最左位置（有序数组二分）
bisect.bisect_right(a, x)
```

## 数学 / 常量
```python
float('inf'), float('-inf')
divmod(a, b)                   # 返回 (a//b, a%b)
import math
math.gcd(a, b); math.inf; math.isqrt(n)
```

## 链表 / 树节点（自构建 case 时手写）
```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```

## 递归深度（DFS 深的时候笔试会爆栈）
```python
import sys
sys.setrecursionlimit(10**6)
```
