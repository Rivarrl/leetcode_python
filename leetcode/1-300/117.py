# -*- coding: utf-8 -*-
# ======================================
# @File    : 117.py
# @Time    : 2020/9/28 0:04
# @Author  : Rivarrl
# ======================================
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)
    """
    def connect(self, root: 'Node') -> 'Node':
        def f(root, parent=None, d=0):
            if not root: return root
            if parent:
                if d == 1 and parent.right:
                    root.next = parent.right
                else:
                    while parent.next:
                        parent = parent.next
                        if parent.left:
                            root.next = parent.left
                            break
                        if parent.right:
                            root.next = parent.right
                            break
            root.right = f(root.right, root, 0)
            root.left = f(root.left, root, 1)
            return root
        return f(root)

if __name__ == '__main__':
    a = Solution()
    arr = [1,2,3,4,5,None,7]
    n = len(arr)
    def down(i):
        l, r = i*2+1, i*2+2
        root = Node(arr[i])
        if l < n: root.left = down(l)
        if r < n: root.right = down(r)
        return root
    x = down(0)
    res = a.connect(x)
    def display(x):
        while x:
            p = x
            while p:
                if p.val: print(p.val, end=',')
                p = p.next
            x = x.left
            print('#,' if x else '#', end='')
    display(res)