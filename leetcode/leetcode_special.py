from collections import deque
from algorithm_utils import *

# 146. LRU缓存机制
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

# 232. 用栈实现队列
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stk1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stk2:
            return self.stk2.pop()
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        res = self.stk2.pop()
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stk1[0] if self.stk1 else self.stk2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stk1 == [] and self.stk2 == []



# 225. 用队列实现栈
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            while self.q1:
                a = self.q1.pop(0)
                if self.q1:
                    self.q2.append(a)
                else:
                    return a
        else:
            while self.q2:
                a = self.q2.pop(0)
                if self.q2:
                    self.q1.append(a)
                else:
                    return a

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            return self.q1[-1]
        return self.q2[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1 == [] and self.q2 == []


# 297. 二叉树的序列化与反序列化
class Codec:
    """
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    示例: 
    你可以将以下二叉树：
        1
       / \
      2   3
         / \
        4   5
    序列化为 "[1,2,3,null,null,4,5]"
    提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
    说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if root:
            stk = [root]
            while stk:
                x = stk.pop()
                res.append(' ')
                if x:
                    res.append(str(x.val))
                    stk.insert(0, x.left)
                    stk.insert(0, x.right)
                else:
                    res.append('None')
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data: return None
        tree_data = data.strip().split()
        if tree_data[0] == 'None': return None
        root = TreeNode(int(tree_data[0]))
        stk = [root]
        i = 1
        while stk:
            x = stk.pop()
            if not x:
                continue
            x.left = TreeNode(int(tree_data[i])) if tree_data[i] != "None" else None
            x.right = TreeNode(int(tree_data[i+1])) if tree_data[i+1] != "None" else None
            i += 2
            stk.insert(0, x.left)
            stk.insert(0, x.right)
        return root


# 173. 二叉搜索树迭代器
# 中序遍历二叉搜索树, 拉成只有right的搜索树
class BSTIterator:
    """
    实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
    调用 next() 将返回二叉搜索树中的下一个最小的数。
    示例：
        7
       3,15
      ,,9,20

    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // 返回 3
    iterator.next();    // 返回 7
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 9
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 15
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 20
    iterator.hasNext(); // 返回 false
    提示：
    next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
    你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
    """
    def __init__(self, root: TreeNode):
        self.root = None
        self.last = None
        if root: self.dfs(root)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.root.val
        self.root = self.root.right
        return val


    def dfs(self, node) -> None:
        if node.left:
            self.dfs(node.left)
        if self.last:
            node.left = None
            self.last.right = node
        else:
            self.root = node
        self.last = node
        if node.right:
            self.dfs(node.right)


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.root


# 173. 二叉搜索树迭代器
# 中序遍历二叉搜索树, 用stack
class BSTIterator_Stack:
    def __init__(self, root: TreeNode):
        self.stk = []
        self.push(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.stk.pop()
        if cur.right:
            self.push(cur.right)
        return cur.val


    def push(self, node) -> None:
        while node and node.left:
            self.stk.append(node)
            node = node.left
        return node


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stk)


# 173. 二叉搜索树迭代器
# 中序莫里斯遍历
class BSTIterator_Morris:
    def __init__(self, root: TreeNode):
        self.cur = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = 0
        while self.cur:
            if self.cur.left:
                pre = self.cur.left
                while pre.right and pre.right != self.cur:
                    pre = pre.right
                if pre.right:
                    pre.right = None
                    res = self.cur.val
                    self.cur = self.cur.right
                    break
                else:
                    pre.right = self.cur
                    self.cur = self.cur.left
            else:
                res = self.cur.val
                self.cur = self.cur.right
                break
        return res


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.cur)


# 398. 随机数索引
# hashmap + list
class RandomIndex:
    """
    给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
    注意：
    数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
    示例:
    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);
    // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
    solution.pick(3);
    // pick(1) 应该返回 0。因为只有nums[0]等于1。
    solution.pick(1);
    """
    def __init__(self, nums):
        from collections import defaultdict
        self.map = defaultdict(list)
        self.imap = {}
        for i, x in enumerate(nums):
            self.map[x].append(i)
            if not x in self.imap:
                self.imap[x] = 0

    def pick(self, target):
        target_list = self.map.get(target)
        ans = target_list[self.imap[target]]
        self.imap[target] = (self.imap[target] + 1) % len(target_list)
        return ans


# 398. 随机数索引
# hashmap + 循环链表
class RandomIndex2:
    def __init__(self, nums):
        self.map = {}
        self.temp = {}
        for i, x in enumerate(nums):
            cur = ListNode(i)
            if not x in self.map:
                self.map[x] = cur
            else:
                last = self.temp[x]
                last.next = cur
            self.temp[x] = cur
        for k, v in self.temp.items():
            v.next = self.map[k]
        self.temp.clear()

    def pick(self, target):
        ans = self.map[target].val
        self.map[target] = self.map[target].next
        return ans


if __name__ == '__main__':
    x = construct_tree_node([4,2,6,1,3,5,7])
    bs = BSTIterator_Morris(x)
    while bs.hasNext():
        print(bs.next())
    # x = construct_tree_node([5,2,3,null,null,2,4,null,null,null,null,3,1])
    # codec = Codec()
    # y = codec.deserialize(codec.serialize(x))
    # print_tree_node(x)
    # print_tree_node(y)
    pass