# -*- coding:utf-8 -*-
from algorithm_utils import *
# leetcode 简单题 5

def leafSimilar(root1, root2):
    """
    872. 叶子相似的树
    请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
          3
       5     1
      6 2   9 8
       7 4
    举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
    如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
    如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
    提示：
    给定的两颗树可能会有 1 到 100 个结点。
    :param root1: TreeNode
    :param root2: TreeNode
    :return: bool
    """
    def helper(node):
        if node:
            if not node.left and not node.right:
                yield node.val
            else:
                yield from helper(node.left)
                yield from helper(node.right)

    for x, y in zip(helper(root1), helper(root2)):
        if x != y:
            return False
    return True


if __name__ == '__main__':
    x, y = construct_tree_node([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), construct_tree_node([2, 3, 5, 6, 1, 9, 8, null, null, 7, 4])
    leafSimilar(x, y)
    # x, y = construct_tree_node([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), construct_tree_node([2, 3, 5, 6, 1, 9, 8, null, null, 7, 0])
    # leafSimilar(x, y)
    pass