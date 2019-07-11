# -*- coding:utf-8 -*-
from algorithm_utils import *


# leetcode 7

def countNodes(root):
    """
    222. 完全二叉树的节点个数
    给出一个完全二叉树，求出该树的节点个数。
    说明：
    完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
    示例:
    输入:
        1
       / \
      2   3
     / \  /
    4  5 6
    输出: 6
    :param root: TreeNode
    :return: int
    """

    def helper(p, lv):
        if par[1]: return
        if lv < level - 1:
            helper(p.left, lv + 1)
            helper(p.right, lv + 1)
        else:
            if p.left and p.right:
                par[0] += 2
            else:
                if p.left:
                    par[0] += 1
                par[1] = True

    p = root
    level = 0
    while p:
        level += 1
        p = p.left
    if level <= 1: return level
    par = [2 ** (level - 1) - 1, False]
    helper(root, 1)
    return par[0]


def computeArea(A, B, C, D, E, F, G, H):
    """
    223. 矩形面积
    在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
    每个矩形由其左下顶点和右上顶点坐标表示
    示例:
    输入: -3, 0, 3, 4, 0, -1, 9, 2
    输出: 45
    说明: 假设矩形面积不会超出 int 的范围。
    :param A: int
    :param B: int
    :param C: int
    :param D: int
    :param E: int
    :param F: int
    :param G: int
    :param H: int
    :return: int
    """
    # 两个矩形面积和减去重叠部分面积
    get_D = lambda x1, x2: abs(x2 - x1)
    get_S = lambda x1, y1, x2, y2: get_D(x1, x2) * get_D(y1, y2)
    S1 = get_S(A, B, C, D)
    S2 = get_S(E, F, G, H)
    S3 = 0
    D_AC = get_D(A, C)
    D_EG = get_D(E, G)
    D_12 = max(get_D(min(A, C), max(E, G)), get_D(min(E, G), max(A, C)))
    D_BD = get_D(B, D)
    D_FH = get_D(F, H)
    D_34 = max(get_D(min(B, D), max(F, H)), get_D(min(F, H), max(B, D)))
    if (min(A, C) <= min(E, G) <= max(E, G) <= max(A, C) and min(B, D) <= min(F, H) <= max(F, H) <= max(B, D)) or (min(E, G) <= min(A, C) <= max(A, C) <= max(E, G) and min(F, H) <= min(B, D) <= max(B, D) <= max(F, H)):
        return max(S1, S2)
    if not (D_12 > D_AC + D_EG and D_34 > D_BD + D_FH):
        S3 = min(get_D(min(A, C), max(E, G)), get_D(min(E, G), max(A, C))) * min(get_D(min(B, D), max(F, H)), get_D(min(F, H), max(B, D)))
    ans = S1 + S2 - S3
    print(S1, S2, S3)
    print(ans)
    return ans


if __name__ == '__main__':
    # x = construct_tree_node([1,2,3,4,5,6])
    # countNodes(x)
    computeArea(0, 0, 1, 1, 1, 1, 2, 2)
    computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    computeArea(0, 0, 0, 0, -1, -1, 1, 1)
    computeArea(-1, -1, 1, 1, -2, -2, 2, 2)
    computeArea(0, 0, 3, 1, 1, 0, 4, 1)
    computeArea(-2, -2, 2, 2, -3, -3, 3, -1)
    pass
