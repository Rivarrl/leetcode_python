# -*- coding: utf-8 -*-
# ======================================
# @File    : 707.py
# @Time    : 2019/12/6 14:10
# @Author  : Rivarrl
# ======================================

class Node:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length == 0 or index < 0 or index >= self.length: return -1
        elif index == 0: return self.head.val
        elif index == self.length - 1: return self.tail.val
        else:
            p = self.head
            for i in range(index):
                p = p.next
            return p.val

    def addFirst(self, val):
        self.head = self.tail = Node(val)
        self.length += 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.length == 0: self.addFirst(val)
        else:
            tmp = self.head
            self.head = Node(val)
            tmp.pre = self.head
            self.head.next = tmp
            self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.length == 0: self.addFirst(val)
        else:
            self.tail.next = Node(val)
            tmp = self.tail
            self.tail = self.tail.next
            self.tail.pre = tmp
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length: return
        elif index <= 0: self.addAtHead(val)
        elif index == self.length: self.addAtTail(val)
        else:
            p = self.head
            for i in range(index-1):
                p = p.next
            q = Node(val)
            q.next = p.next
            q.pre = p
            q.next.pre = q
            p.next = q
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.length == 0 or index < 0 or index > self.length - 1: return
        elif index == 0:
            self.head = self.head.next
            if self.head: self.head.pre = None
        elif index == self.length - 1:
            self.tail = self.tail.pre
            if self.tail: self.tail.next = None
        else:
            p = self.head
            for i in range(index):
                p = p.next
            p.pre.next = p.next
            p.next.pre = p.pre
        self.length -= 1


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.deleteAtIndex(0)
