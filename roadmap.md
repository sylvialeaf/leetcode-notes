# 刷题题单 · 学习路线（融合 labuladong 路线图 + 灵茶分类 + CodeTop 高频）

> 顺序参考 labuladong 算法路线图（https://labuladong.online/zh/roadmap/algo/）；
> 分类对照见 `solutions/categories.md`；资源分工见 `资料来源.md`。

## 怎么用这份题单

**两阶段 + 融合打法**：

1. **阶段一·分类突破（现在做）**：按下面顺序，一类一类刷。**同类连着做，套路才能记住**。每类里 **先做 ⭐高频题，再做普通题**（这就是"用 CodeTop 频率给同类剪枝"的融合打法），低频偏题可先跳过。
2. **阶段二·高频冲刺（快面试时做）**：去 CodeTop 按目标公司乱序刷高频，模拟真实面试。

**每题怎么做**：复制 `solutions/_TEMPLATE.py` → 改名为题目英文名放进对应**本地文件夹** → 点开 **LeetCode 链接** 读题 → 自己造 case 写完跑通 → 去 `progress/刷题记录.md` 标掌握度。

**标记说明**：⭐=CodeTop 高频必做　难度 简/中/难　✅=我已带你建好样板。

---

# 阶段一 · 分类突破（按 labuladong 顺序）

## 0. 起步样板（已建好，先读懂这 3 个）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 215 | 数组中第K大元素 | 中 ✅⭐ | `solutions/heap/` | https://leetcode.cn/problems/kth-largest-element-in-an-array/ |
| 46 | 全排列 | 中 ✅⭐ | `solutions/backtracking/` | https://leetcode.cn/problems/permutations/ |
| 146 | LRU 缓存 | 中 ✅⭐ | `solutions/design/` | https://leetcode.cn/problems/lru-cache/ |

## 1. 数组 · 双指针（最基础，先建立手感）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 704 | 二分查找 | 简 | `solutions/binary_search/` | https://leetcode.cn/problems/binary-search/ |
| 27 | 移除元素 | 简 | `solutions/array/` | https://leetcode.cn/problems/remove-element/ |
| 26 | 删除有序数组中的重复项 | 简 | `solutions/array/` | https://leetcode.cn/problems/remove-duplicates-from-sorted-array/ |
| 283 | 移动零 | 简 ⭐ | `solutions/array/` | https://leetcode.cn/problems/move-zeroes/ |
| 167 | 两数之和 II（有序） | 中 | `solutions/two_pointers/` | https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/ |
| 15 | 三数之和 | 中 ⭐ | `solutions/two_pointers/` | https://leetcode.cn/problems/3sum/ |
| 11 | 盛最多水的容器 | 中 ⭐ | `solutions/two_pointers/` | https://leetcode.cn/problems/container-with-most-water/ |

## 2. 滑动窗口
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 209 | 长度最小的子数组 | 中 | `solutions/sliding_window/` | https://leetcode.cn/problems/minimum-size-subarray-sum/ |
| 3 | 无重复字符的最长子串 | 中 ⭐ | `solutions/sliding_window/` | https://leetcode.cn/problems/longest-substring-without-repeating-characters/ |
| 438 | 找到字符串中所有字母异位词 | 中 | `solutions/sliding_window/` | https://leetcode.cn/problems/find-all-anagrams-in-a-string/ |
| 567 | 字符串的排列 | 中 | `solutions/sliding_window/` | https://leetcode.cn/problems/permutation-in-string/ |
| 76 | 最小覆盖子串 | 难 ⭐ | `solutions/sliding_window/` | https://leetcode.cn/problems/minimum-window-substring/ |

## 3. 二分查找（重点练"边界"）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 35 | 搜索插入位置 | 简 | `solutions/binary_search/` | https://leetcode.cn/problems/search-insert-position/ |
| 34 | 在排序数组中查找元素的第一个和最后一个位置 | 中 ⭐ | `solutions/binary_search/` | https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 33 | 搜索旋转排序数组 | 中 ⭐ | `solutions/binary_search/` | https://leetcode.cn/problems/search-in-rotated-sorted-array/ |
| 153 | 寻找旋转排序数组中的最小值 | 中 | `solutions/binary_search/` | https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/ |
| 875 | 爱吃香蕉的珂珂（二分答案） | 中 | `solutions/binary_search/` | https://leetcode.cn/problems/koko-eating-bananas/ |

## 4. 前缀和 · 差分
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 303 | 区域和检索 - 数组不可变 | 简 | `solutions/prefix_sum/` | https://leetcode.cn/problems/range-sum-query-immutable/ |
| 560 | 和为 K 的子数组 | 中 ⭐ | `solutions/prefix_sum/` | https://leetcode.cn/problems/subarray-sum-equals-k/ |
| 1109 | 航班预订统计（差分） | 中 | `solutions/prefix_sum/` | https://leetcode.cn/problems/corporate-flight-bookings/ |

## 5. 链表（面试高频区，必扎实）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 206 | 反转链表 | 简 ⭐ | `solutions/linked_list/` | https://leetcode.cn/problems/reverse-linked-list/ |
| 21 | 合并两个有序链表 | 简 ⭐ | `solutions/linked_list/` | https://leetcode.cn/problems/merge-two-sorted-lists/ |
| 160 | 相交链表 | 简 | `solutions/linked_list/` | https://leetcode.cn/problems/intersection-of-two-linked-lists/ |
| 142 | 环形链表 II | 中 ⭐ | `solutions/linked_list/` | https://leetcode.cn/problems/linked-list-cycle-ii/ |
| 19 | 删除链表的倒数第 N 个结点 | 中 | `solutions/linked_list/` | https://leetcode.cn/problems/remove-nth-node-from-end-of-list/ |
| 92 | 反转链表 II | 中 | `solutions/linked_list/` | https://leetcode.cn/problems/reverse-linked-list-ii/ |
| 234 | 回文链表 | 简 | `solutions/linked_list/` | https://leetcode.cn/problems/palindrome-linked-list/ |
| 25 | K 个一组翻转链表 | 难 ⭐ | `solutions/linked_list/` | https://leetcode.cn/problems/reverse-nodes-in-k-group/ |
| 23 | 合并 K 个升序链表 | 难 ⭐ | `solutions/linked_list/` | https://leetcode.cn/problems/merge-k-sorted-lists/ |

## 6. 栈 · 队列 · 单调栈
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 20 | 有效的括号 | 简 ⭐ | `solutions/stack/` | https://leetcode.cn/problems/valid-parentheses/ |
| 155 | 最小栈 | 中 ⭐ | `solutions/stack/` | https://leetcode.cn/problems/min-stack/ |
| 232 | 用栈实现队列 | 简 | `solutions/queue/` | https://leetcode.cn/problems/implement-queue-using-stacks/ |
| 739 | 每日温度 | 中 ⭐ | `solutions/monotonic_stack/` | https://leetcode.cn/problems/daily-temperatures/ |
| 496 | 下一个更大元素 I | 简 | `solutions/monotonic_stack/` | https://leetcode.cn/problems/next-greater-element-i/ |
| 84 | 柱状图中最大的矩形 | 难 | `solutions/monotonic_stack/` | https://leetcode.cn/problems/largest-rectangle-in-histogram/ |

## 7. 哈希
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 1 | 两数之和 | 简 ⭐ | `solutions/hash/` | https://leetcode.cn/problems/two-sum/ |
| 49 | 字母异位词分组 | 中 ⭐ | `solutions/hash/` | https://leetcode.cn/problems/group-anagrams/ |
| 128 | 最长连续序列 | 中 ⭐ | `solutions/hash/` | https://leetcode.cn/problems/longest-consecutive-sequence/ |

## 8. 堆 · 优先队列
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 347 | 前 K 个高频元素 | 中 ⭐ | `solutions/heap/` | https://leetcode.cn/problems/top-k-frequent-elements/ |
| 295 | 数据流的中位数 | 难 ⭐ | `solutions/heap/` | https://leetcode.cn/problems/find-median-from-data-stream/ |

## 9. 二叉树 ⭐⭐ labuladong 核心（务必练透，是后面回溯/BFS/DP 的地基）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 94 | 二叉树的中序遍历 | 简 | `solutions/tree/` | https://leetcode.cn/problems/binary-tree-inorder-traversal/ |
| 104 | 二叉树的最大深度 | 简 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/maximum-depth-of-binary-tree/ |
| 226 | 翻转二叉树 | 简 | `solutions/tree/` | https://leetcode.cn/problems/invert-binary-tree/ |
| 102 | 二叉树的层序遍历 | 中 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/binary-tree-level-order-traversal/ |
| 543 | 二叉树的直径 | 简 | `solutions/tree/` | https://leetcode.cn/problems/diameter-of-binary-tree/ |
| 114 | 二叉树展开为链表 | 中 | `solutions/tree/` | https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/ |
| 105 | 从前序与中序遍历序列构造二叉树 | 中 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ |
| 236 | 二叉树的最近公共祖先 | 中 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/ |
| 124 | 二叉树中的最大路径和 | 难 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/binary-tree-maximum-path-sum/ |

## 10. 二叉搜索树 BST
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 700 | 二叉搜索树中的搜索 | 简 | `solutions/tree/` | https://leetcode.cn/problems/search-in-a-binary-search-tree/ |
| 98 | 验证二叉搜索树 | 中 ⭐ | `solutions/tree/` | https://leetcode.cn/problems/validate-binary-search-tree/ |
| 230 | 二叉搜索树中第 K 小的元素 | 中 | `solutions/tree/` | https://leetcode.cn/problems/kth-smallest-element-in-a-bst/ |
| 450 | 删除二叉搜索树中的节点 | 中 | `solutions/tree/` | https://leetcode.cn/problems/delete-node-in-a-bst/ |

## 11. 图论 · 网格
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 200 | 岛屿数量 | 中 ⭐ | `solutions/grid_graph/` | https://leetcode.cn/problems/number-of-islands/ |
| 994 | 腐烂的橘子 | 中 | `solutions/grid_graph/` | https://leetcode.cn/problems/rotting-oranges/ |
| 207 | 课程表（拓扑排序） | 中 ⭐ | `solutions/graph/` | https://leetcode.cn/problems/course-schedule/ |
| 210 | 课程表 II | 中 | `solutions/graph/` | https://leetcode.cn/problems/course-schedule-ii/ |
| 547 | 省份数量（并查集） | 中 | `solutions/union_find/` | https://leetcode.cn/problems/number-of-provinces/ |

## 12. 回溯 DFS（= 多叉树遍历）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 78 | 子集 | 中 ⭐ | `solutions/backtracking/` | https://leetcode.cn/problems/subsets/ |
| 77 | 组合 | 中 | `solutions/backtracking/` | https://leetcode.cn/problems/combinations/ |
| 39 | 组合总和 | 中 | `solutions/backtracking/` | https://leetcode.cn/problems/combination-sum/ |
| 22 | 括号生成 | 中 ⭐ | `solutions/backtracking/` | https://leetcode.cn/problems/generate-parentheses/ |
| 79 | 单词搜索 | 中 | `solutions/backtracking/` | https://leetcode.cn/problems/word-search/ |
| 51 | N 皇后 | 难 | `solutions/backtracking/` | https://leetcode.cn/problems/n-queens/ |

## 13. BFS（= 层序遍历）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 111 | 二叉树的最小深度 | 简 | `solutions/tree/` | https://leetcode.cn/problems/minimum-depth-of-binary-tree/ |
| 752 | 打开转盘锁 | 中 | `solutions/graph/` | https://leetcode.cn/problems/open-the-lock/ |
| 127 | 单词接龙 | 难 | `solutions/graph/` | https://leetcode.cn/problems/word-ladder/ |

## 14. 动态规划 ⭐⭐（最难，放最后，慢慢啃）
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 509 | 斐波那契数（入门） | 简 | `solutions/dp/` | https://leetcode.cn/problems/fibonacci-number/ |
| 70 | 爬楼梯 | 简 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/climbing-stairs/ |
| 53 | 最大子数组和 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/maximum-subarray/ |
| 198 | 打家劫舍 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/house-robber/ |
| 121 | 买卖股票的最佳时机 | 简 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/ |
| 322 | 零钱兑换（完全背包） | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/coin-change/ |
| 416 | 分割等和子集（01背包） | 中 | `solutions/dp/` | https://leetcode.cn/problems/partition-equal-subset-sum/ |
| 300 | 最长递增子序列 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/longest-increasing-subsequence/ |
| 1143 | 最长公共子序列 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/longest-common-subsequence/ |
| 5 | 最长回文子串 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/longest-palindromic-substring/ |
| 64 | 最小路径和 | 中 | `solutions/dp/` | https://leetcode.cn/problems/minimum-path-sum/ |
| 72 | 编辑距离 | 中 ⭐ | `solutions/dp/` | https://leetcode.cn/problems/edit-distance/ |

## 15. 贪心 · 区间
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 55 | 跳跃游戏 | 中 ⭐ | `solutions/greedy/` | https://leetcode.cn/problems/jump-game/ |
| 45 | 跳跃游戏 II | 中 | `solutions/greedy/` | https://leetcode.cn/problems/jump-game-ii/ |
| 56 | 合并区间 | 中 ⭐ | `solutions/greedy/` | https://leetcode.cn/problems/merge-intervals/ |
| 435 | 无重叠区间 | 中 | `solutions/greedy/` | https://leetcode.cn/problems/non-overlapping-intervals/ |

## 16. 杂项 · 位运算 · 设计
| 题号 | 题名 | 难度 | 本地文件夹 | LeetCode 链接 |
|---|---|---|---|---|
| 136 | 只出现一次的数字 | 简 ⭐ | `solutions/bit_manipulation/` | https://leetcode.cn/problems/single-number/ |
| 191 | 位 1 的个数 | 简 | `solutions/bit_manipulation/` | https://leetcode.cn/problems/number-of-1-bits/ |

---

# 阶段二 · 高频冲刺（快面试时再做）

这一阶段**不列静态题单**，因为高频榜会变、且要按你的目标公司定。做法：

1. 打开 CodeTop：https://codetop.cc/home
2. 选你的**目标公司**（或全站），按**出现频率从高到低**排序。
3. **乱序刷前 100 题**，模拟真实面试"不知道下一题是啥"的感觉。
4. 遇到不会的，回到阶段一对应分类补一补。

> 阶段一把上面 ⭐ 的题刷完，其实已经覆盖了 CodeTop 高频的大半，阶段二主要是查漏补缺 + 适应乱序。

---

# 进度追踪

- 做完一题：去 `progress/刷题记录.md` 标 🔴/🟡/🟢 掌握度。
- 一个模块做完：回这里在标题前打个勾（如 `## 1. 数组 · 双指针 ✅`）。
- 复习：🔴🟡 的题按 1/3/7/14 天重做，只看思路注释能否还原代码。
