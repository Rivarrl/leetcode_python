# -*- coding: utf-8 -*-
# ======================================
# @File    : 897.py
# @Time    : 2019/12/1 23:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [897. 递增顺序查找树](https://leetcode-cn.com/problems/increasing-order-search-tree/)
    """
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        中序遍历，把不对的连接调对
        """
        def dfs(p):
            nonlocal pre, res
            if not p: return
            dfs(p.left)
            if pre: pre.right = p
            else: res = p
            p.left, pre = None, p
            dfs(p.right)
        pre = None
        res = None
        dfs(root)
        return res


    def increasingBST2(self, root: TreeNode) -> TreeNode:
        """
        非递归
        """
        stk = []
        res = pre = None
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            p = stk.pop()
            root = p.right
            if pre: pre.right = p
            else: res = p
            p.left, pre = None, p
        return res


    def increasingBST3(self, root: TreeNode) -> TreeNode:
        """
        评论区大佬的代码，学习一下
        我的理解是这样的，我们可以把递归的结果当成已知条件，dfs要做的是把root为根节点的这棵树转为right链表，返回的应该为链表的head
        所以已知dfs(root.left)是一个链表，链表末尾right已经指向root节点
        那么对于root的操作只需要两步：
        root.left=None
        root.right=dfs(root.right)
        现在的问题就是如何让链表返回中序遍历首次访问的head
        根据递归的顺序，第一次调用时的返回值是最终的返回值。
        如果左子树返回的是左子树的链表head，那么当前树只需要把左子返回的结果return就可以了。
        用递归的方式理解就是，最先访问的左节点叫做res，每次只需要把这个res返回即可
        所以有res = dfs(root.left) 和 return res
        最后是这个tail，tail比较难理解，它保存的是递归经过过的节点相对当前节点的中序遍历的下一个节点
        啥意思呢，把一棵树转成链表的过程画出来就明白了。
        通过观察可以发现，除了正确连接的right，其余的操作可分为三种，1) 左子指父，2) 祖先指右子树的最深的左子，3) 叶子节点的右子指祖先
        可以从递归的两种方向讨论：
        1) 对于递归左子(root->root.left)，我们要做的是把左子的right指向父节点，所以要tail是当前节点的父节点，所以有dfs(root.left, root)，对应操作1。
        2) 对于递归右子(root->root.right)，还有两种分支情况：
            1) root还有右子树，那么root的下一个节点是右子树完成dfs之后返回的head，也就是root.right=dfs(root.right)即可，对应操作2
            2) root没有右子树，那么应该有这么一种操作，root.right=tail，tail是root的中序遍历的下一个节点，对应操作3
            这种情况只会发生在一棵树的右子树中最（右侧）大的一个节点，由于BST的特性某节点node的右子树最大值也不会比它的父节点还要大
            所以访问右子的时候把它的父节点值(tail)传给右子树即可，root.right=dfs(root.right, tail)
        由于最后的结果没有left，对每个节点都做一次root.left = None
        比如例子里的那棵树：
               5
              / \
             3   6
            / \   \
           2   4   8
          /       / \
         1       7   9
        访问到1的时候，tail保存的是2节点，1.right = 2
        访问到4的时候，tail保存的是5节点，4.right = 5
        访问到5的时候，先去让他的右子树恢复成链表结构，返回的是head节点6，5.right = 6
        """
        def dfs(root, tail=None):
            if not root: return tail
            res = dfs(root.left, root)
            root.left = None
            root.right = dfs(root.right, tail)
            return res
        return dfs(root)


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,3,6,2,4,null,8,1,null,null,null,null,null,7,9])
    res = a.increasingBST3(x)
    print_tree_node(res)