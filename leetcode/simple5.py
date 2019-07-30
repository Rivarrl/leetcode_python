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


def tribonacci(n):
    """
    1137. 第 N 个泰波那契数
    泰波那契序列 Tn 定义如下： 
    T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
    给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
    示例 1：
    输入：n = 4
    输出：4
    解释：
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4
    示例 2：
    输入：n = 25
    输出：1389537
    提示：
    0 <= n <= 37
    答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
    :param n: int
    :return: int
    """
    t0, t1, t2 = 0, 1, 1
    if n < 3:
        return [t0, t1, t2][n]
    for i in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2


def distributeCandies(candies, num_people):
    """
    1103. 分糖果 II
    排排坐，分糖果。
    我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。
    给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。
    然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。
    重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。
    返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。
    示例 1：
    输入：candies = 7, num_people = 4
    输出：[1,2,3,1]
    解释：
    第一次，ans[0] += 1，数组变为 [1,0,0,0]。
    第二次，ans[1] += 2，数组变为 [1,2,0,0]。
    第三次，ans[2] += 3，数组变为 [1,2,3,0]。
    第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
    示例 2：
    输入：candies = 10, num_people = 3
    输出：[5,2,3]
    解释：
    第一次，ans[0] += 1，数组变为 [1,0,0]。
    第二次，ans[1] += 2，数组变为 [1,2,0]。
    第三次，ans[2] += 3，数组变为 [1,2,3]。
    第四次，ans[0] += 4，最终数组变为 [5,2,3]。
    提示：
    1 <= candies <= 10^9
    1 <= num_people <= 1000
    :param candies: int
    :param num_people: int
    :return: List[int]
    """
    n = 1
    while n * (n + 1) < 2 * candies:
        n += 1
    res = [0] * num_people
    for j in range(n):
        i = j % num_people
        cur = min(j + 1, candies)
        res[i] += cur
        candies -= j + 1
    return res


if __name__ == '__main__':
    distributeCandies(10, 3)
    # tribonacci(25)
    # x, y = construct_tree_node([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), construct_tree_node([2, 3, 5, 6, 1, 9, 8, null, null, 7, 0])
    # leafSimilar(x, y)
    pass
