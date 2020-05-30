# -*- coding: utf-8 -*-
# ======================================
# @File    : 84.py
# @Time    : 2020/5/30 9:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class SegmentTreeNode:
    # 线段树节点，mi存储min值的下标
    def __init__(self, start, end, mi, left=None, right=None):
        self.start = start
        self.end = end
        self.mi = mi
        self.left = left
        self.right = right


class Solution:
    """
    [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
    """
    @timeit
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 分治法 + 线段树
        def build_tree(left, right):
            if left > right: return
            root = SegmentTreeNode(left, right, left)
            if left == right: return root
            mid = (left + right) // 2
            root.left = build_tree(left, mid)
            root.right = build_tree(mid + 1, right)
            if heights[root.left.mi] < heights[root.right.mi]:
                root.mi = root.left.mi
            else:
                root.mi = root.right.mi
            return root

        def query_tree(root, start, end):
            if start > root.end or end < root.start: return -1
            if start <= root.start and end >= root.end: return root.mi
            left_mi = query_tree(root.left, start, end)
            right_mi = query_tree(root.right, start, end)
            if left_mi < 0: return right_mi
            if right_mi < 0: return left_mi
            if heights[left_mi] < heights[right_mi]:
                return left_mi
            return right_mi

        def dfs(start, end):
            if start > end: return -1
            if start == end: return heights[start]
            i = query_tree(seg_tree, start, end)
            left = dfs(start, i-1)
            right = dfs(i+1, end)
            return max(left, right, (end - start + 1) * heights[i])
        seg_tree = build_tree(0, len(heights) - 1)
        return dfs(0, len(heights) - 1)

    @timeit
    def largestRectangleArea2(self, heights: List[int]) -> int:
        # 单调栈，单增
        stk = []
        heights = [0] + heights + [0]
        n = len(heights)
        res = 0
        for i in range(n):
            while stk and heights[stk[-1]] > heights[i]:
                j = stk.pop()
                res = max(res, (i - 1 - stk[-1]) * heights[j])
            stk.append(i)
        return res

if __name__ == '__main__':
    a = Solution()
    a.largestRectangleArea2([2,1,5,6,2,3])
    a.largestRectangleArea2([2,1,2])