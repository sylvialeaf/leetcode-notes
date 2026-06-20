"""
题目: LRU 缓存 / LRU Cache    LeetCode 146
链接: https://leetcode.cn/problems/lru-cache/

思路 (面试就讲这三句):
  1. 本质是要 get/put 都 O(1)，且能 O(1) 淘汰"最久未使用"的设计题。
  2. 用【哈希表 + 双向链表】：哈希表 key→节点 实现 O(1) 查找；双向链表按使用
     顺序排列，最近用的放头部、最久未用的在尾部，淘汰就删尾。关键：每次访问把
     节点移到头部。手写双向链表配 dummy 头尾哨兵节点，删除/插入不用判空。
  3. get/put 均摊 O(1)，空间 O(capacity)。

易错点:
  - 一定用【双向】链表，单链表删节点要找前驱、做不到 O(1)。
  - 用 dummy head/tail 哨兵，省掉一堆边界判断。
  - put 已存在的 key 要更新值并移到头部，别只更新值。

掌握度: 🟢 (示例题，已写好；面试常考，建议手写而非用 OrderedDict)

注: Python 有 collections.OrderedDict 可秒解，但面试官常要求手写双向链表，这里手写。
"""


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                 # key -> Node
        self.head, self.tail = Node(), Node()   # 哨兵
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node: Node):   # 加到头部(最近使用)
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)           # 访问即提到最前
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return
        if len(self.cache) == self.cap:           # 满了淘汰尾部
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        node = Node(key, value)
        self.cache[key] = node
        self._add_front(node)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # 1
    lru.put(3, 3)        # 淘汰 key 2
    print(lru.get(2))   # -1
    lru.put(4, 4)        # 淘汰 key 1
    print(lru.get(1))   # -1
    print(lru.get(3))   # 3
    print(lru.get(4))   # 4
