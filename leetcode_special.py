


from collections import deque

# （慢） 优先队列 + 哈希表， get操作时的查找耗时较大
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.deque = deque()
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ans = -1
        if key in self.cache:
            ans = self.cache[key]
            self.deque.remove(key)
            self.deque.appendleft(key)
        return ans

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            self.deque.appendleft(key)
        else:
            self.deque.remove(key)
            self.deque.appendleft(key)
        self.cache[key] = value
        if self.deque.__len__() > self.capacity:
            p = self.deque.pop()
            self.cache.pop(p)


class Node(object):

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

# LRU 双向链表 + 哈希表
class LRUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        if node.next != None:
            if node.prev == None:
                # head
                self.head = self.head.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            self.node_map[key].val = value
            self.get(key)
            return
        if len(self.node_map) == self.capacity:
            node = self.node_map[self.head.key]
            del self.node_map[self.head.key]
            self.node_map[key] = node
            node.val = value
            node.key = key
            self.get(key)
        else:
            node = Node(key, value)
            self.node_map[key] = node
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node