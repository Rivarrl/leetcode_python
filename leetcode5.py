# -*- coding:utf-8 -*-

from algorithm_utils import *

# leetcode5

def canCompleteCircuit(gas, cost):
    """
    134. 加油站
    在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
    你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
    如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
    说明:
    如果题目有解，该答案即为唯一答案。
    输入数组均为非空数组，且长度相同。
    输入数组中的元素均为非负数。
    示例 1:
    输入:
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    输出: 3
    解释:
    从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
    开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
    开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
    开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
    开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
    开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
    因此，3 可为起始索引。
    示例 2:
    输入:
    gas  = [2,3,4]
    cost = [3,4,3]
    输出: -1
    解释:
    你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
    我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
    开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
    开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
    你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
    因此，无论怎样，你都不可能绕环路行驶一周。
    :param gas: List[int]
    :param cost: List[int]
    :return: int
    """
    """
    # 贪心算法
    n = len(gas)
    rs = []
    for i in range(n):
        rs.append(gas[i] - cost[i])
    if sum(rs) < 0: return -1
    m, res = -1, -1
    for j in range(n):
        if j == 0:
            if rs[0] - rs[-1] > m:
                m = rs[0] - rs[-1]
                res = j
        else:
            if rs[j] - rs[j-1] > m:
                m = rs[j] - rs[j-1]
                res = j
    return res
    """
    # 优化，根据刚才的rs数组找max(rs[i] - rs[i-1])得知，只要找到一个求和记录中的最小值，它的下一个位置就是起始点(在最终rs值非负的情况下，如果rs走完一圈是负值就走不完一圈)
    n = len(gas)
    rs, m = 0, 0
    res = -1
    for i in range(n):
        rs += gas[i] - cost[i]
        if rs < m:
            m = rs
            res = i
    return -1 if rs < 0 else res + 1


def levelOrder(root):
    """
    102. 二叉树的层次遍历
    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
    例如:
    给定二叉树: [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：
    [
      [3],
      [9,20],
      [15,7]
    ]
    :param root: TreeNode
    :return: List[List[int]]
    """
    """
    # 迭代 栈
    res = []
    if root:
        res.append([root.val])
        stk = [root]
        while stk:
            cur = []
            for each in stk:
                if each.right:
                    cur.append(each.right)
                if each.left:
                    cur.append(each.left)
            if cur != []:
                res.append([x.val for x in cur][::-1])
            stk = [x for x in cur]
    print(res)
    return res
    """
    # 迭代 队列
    from collections import deque
    res = []
    if root:
        q = deque()
        q.append(root)
        level = 0
        while q:
            n = len(q)
            res.append([])
            for i in range(n):
                p = q.popleft()
                res[level].append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            level += 1
    return res


def setZeroes(matrix):
    """
    73. 矩阵置零
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
    示例 1:
    输入:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    示例 2:
    输入:
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    输出:
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    进阶:
    一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？
    :param matrix: List[List[int]]
    :return: None
    """
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                continue
            if matrix[i][j] == 0:
                for k in range(m):
                    matrix[i][k] = '0' if matrix[i][k] != 0 else 0
                for q in range(n):
                    matrix[q][j] = '0' if matrix[q][j] != 0 else 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                matrix[i][j] = 0


if __name__ == '__main__':
    x = [[0,1,2,0],
         [3,4,5,2],
         [1,3,1,5]]
    setZeroes(x)
    # x = construct_tree_node([3,9,20,None,None,15,7])
    # levelOrder(x)
    # print(canCompleteCircuit([3,3,4],[3,4,4]))
    pass