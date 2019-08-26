# -*- coding:utf-8 -*-
from algorithm_utils import *

# 二叉树相关

def in_order_visit_morris(root):
    """
    二叉树的Morris中序遍历
    该遍历为非递归且不用栈的遍历, 利用叶节点为空的right, 指向其后继节点
    按左根右的遍历顺序, 根的前驱节点为左子的最右子节点
    参考博客: https://blog.csdn.net/shoulinjun/article/details/19051503
    :param root: TreeNode
    :return: List[int]
    """
    res = []
    while root:
        # 如果无左子, 直接访问
        if not root.left:
            res.append(root.val)
            root = root.right
            continue
        # 否则去左子找root的前驱结点
        pre = root.left
        while pre.right and pre.right != root:
            pre = pre.right
        # 第一次访问pre
        if not pre.right:
            pre.right = root
            root = root.left
        # 第二次访问, 说明左子树已经访问过
        else:
            pre.right = None
            res.append(root.val)
            root = root.right
    return res


if __name__ == '__main__':
    x = construct_tree_node([4,2,6,1,3,5,7])
    res = in_order_visit_morris(x)
    print(res)