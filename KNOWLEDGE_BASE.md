# 📚 力扣刷题知识库（总入口）

> 这是整个 `H:\leetcode` 知识库的总索引。换电脑/换账号，带着这个文件夹就全在。
> 配套带教陪练：跟我说「带我做 XX」「今天复习」「追问我」即可（`leetcode-mentor` skill）。

## 🗂️ 知识库的四层结构

| 层 | 位置 | 是什么 | 什么时候看 |
|---|---|---|---|
| **题单地图** | `roadmap.md` | 刷什么、什么顺序（labuladong 路线 + 灵茶分类 + CodeTop⭐高频） | 决定下一题做什么 |
| **进度账本** | `progress/刷题记录.md` | 掌握度🔴🟡🟢 + 艾宾浩斯复习清单（1/3/7/14 天） | 每天看该复习哪些 |
| **单题三件套** | `solutions/<分类>/<题号>_<名>/` | `problem.md`(原题) + `solution.py`(代码) + `notes.md`(7 小节精炼笔记) | 做题 / 速查某题 |
| **带教全记录** | `lessons/<题号>_..._full_lesson.md` | 完整 QA 对话：我问什么、你答什么、卡在哪、怎么讲通、踩坑、自测 | 复习"当时怎么想的"，对"总是忘"最有效 |
| **跨题速查** | `cheatsheet/` | 不属于单题的通用知识（踩坑/语言概念/复杂度/各类套路） | 卡在通用知识时 |

> **notes.md（精炼速查） vs full_lesson.md（完整全记录）**：notes 是结论速查，full_lesson 保留完整思考过程。复习先看 full_lesson 回忆"怎么想通的"，临场速查看 notes。

## ✅ 已完成专题

### 二分查找 binary_search（6/6 ✅ 全通关）
| 题 | 难度 | 一句话核心 | 三件套 | 全记录 |
|---|---|---|---|---|
| 704 二分查找 | 简 | 二分骨架，找值 | [solutions](solutions/binary_search/704_binary_search/) | [lesson](lessons/704_binary_search_full_lesson.md) |
| 35 搜索插入位置 | 简 | 插入位置=比 target 小的数个数，return left | [solutions](solutions/binary_search/35_search_insert_position/) | [lesson](lessons/35_search_insert_position_full_lesson.md) |
| 34 第一个和最后一个位置 | 中⭐ | 两次二分找左右边界，命中记 ans=mid 不返回 | [solutions](solutions/binary_search/34_find_first_and_last/) | [lesson](lessons/34_find_first_and_last_full_lesson.md) |
| 33 搜索旋转排序数组 | 中⭐ | 判哪半边升序，target 夹区间决定缩哪边 | [solutions](solutions/binary_search/33_search_rotated/) | [lesson](lessons/33_search_rotated_full_lesson.md) |
| 153 旋转数组最小值 | 中 | 模板二：while left<right + right=mid | [solutions](solutions/binary_search/153_find_min_rotated/) | [lesson](lessons/153_find_min_rotated_full_lesson.md) |
| 875 爱吃香蕉的珂珂 | 中⭐ | 二分答案：在值域上二分 + check 判定 | [solutions](solutions/binary_search/875_koko_eating_bananas/) | [lesson](lessons/875_koko_eating_bananas_full_lesson.md) |

**专题速查**：`solutions/binary_search/binary_search.py`（通用模板）、`cheatsheet/踩坑与基础概念.md` 第五节（两套模板 + 二分答案套路）。

## 📅 复习清单（详见 progress/刷题记录.md）
- 704 / 35 / 34：第 3 天复习期（2026-06-12），只看 notes/lesson 思路、默写代码升 🟢。
- 33 / 153 / 875：排在 2026-06-13 左右。

## 🔜 下一步
按 `roadmap.md` 顺序，二分之后进 哈希 / 双指针 等专题。

## ☁️ 个人知识库同步
带教全记录也同步到了我的飞书个人知识库，手机 / 网页随时翻。具体节点映射与同步登记见本地 `feishu_sync_index.md`（私人文件，未纳入公开仓库）。
