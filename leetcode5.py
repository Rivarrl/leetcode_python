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


def exist(board, word):
    """
    79. 单词搜索
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    示例:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.
    :param board: List[List[str]]
    :param word: str
    :return: bool
    """
    def dfs(i, j, k):
        if k == w: return True
        res = False
        visited[i][j] = True
        if not res and i > 0 and board[i-1][j] == word[k] and not visited[i-1][j]:
            res |= dfs(i-1, j, k + 1)
        if not res and j > 0 and board[i][j-1] == word[k] and not visited[i][j-1]:
            res |= dfs(i, j-1, k + 1)
        if not res and i < n - 1 and board[i+1][j] == word[k] and not visited[i+1][j]:
            res |= dfs(i+1, j, k + 1)
        if not res and j < m - 1 and board[i][j+1] == word[k] and not visited[i][j+1]:
            res |= dfs(i, j+1, k + 1)
        visited[i][j] = False
        return res

    n = len(board)
    m = len(board[0])
    w = len(word)
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                if dfs(i, j, 1):
                    return True
    return False


def simplifyPath(path):
    """
    71. 简化路径
    以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
    在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
    请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
    示例 1：
    输入："/home/"
    输出："/home"
    解释：注意，最后一个目录名后面没有斜杠。
    示例 2：
    输入："/../"
    输出："/"
    解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
    示例 3：
    输入："/home//foo/"
    输出："/home/foo"
    解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
    示例 4：
    输入："/a/./b/../../c/"
    输出："/c"
    示例 5：
    输入："/a/../../b/../c//.//"
    输出："/c"
    示例 6：
    输入："/a//b////c/d//././/.."
    输出："/a/b/c"
    :param path: str
    :return: str
    """
    elements = list(filter(lambda x: x and x != '.', path.split('/')))
    print(elements)
    res = []
    for e in elements:
        if e == '..':
            if res:
                res.pop()
        else:
            res.append(e)
    print(res)
    return '/' + '/'.join(res)


def isNumber(s):
    """
    65. 有效数字
    验证给定的字符串是否可以解释为十进制数字。
    例如:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    " -90e3   " => true
    " 1e" => false
    "e3" => false
    " 6e-1" => true
    " 99e2.5 " => false
    "53.5e93" => true
    " --6 " => false
    "-+3" => false
    "95a54e53" => false
    说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
    数字 0-9
    指数 - "e"
    正/负号 - "+"/"-"
    小数点 - "."
    当然，在输入中，这些字符的上下文也很重要。
    :param s: str
    :return: bool
    """
    # 鸡贼写法，正经做法得用DFA，不会，先mark
    try:
        x = float(s.strip())
        return True
    except:
        return False


def maximalRectangle(matrix):
    """
    85. 最大矩形
    给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
    示例:
    输入:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    输出: 6
    :param matrix: List[List[str]]
    :return: int
    """
    # 合并两行求最长连续1长度
    def count1(row):
        res, cur = 0, 0
        for each in row:
            if each == 1:
                cur += 1
            else:
                cur = 0
            if cur > res:
                res = cur
        return res
    res = 0
    n = len(matrix)
    if n > 0:
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        row_multiply = lambda row1, row2: [x * y for x, y in zip(row1, row2)]
        for i in range(n):
            join_row = [1 for _ in range(m)]
            for j in range(i, n):
                cols = j - i + 1
                join_row = row_multiply(join_row, matrix[j])
                cur = cols * count1(join_row)
                if cur > res:
                    res = cur
    return res


def largestRectangleArea(heights):
    """
    84. 柱状图中最大的矩形
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    示例:
    输入: [2,1,5,6,2,3]
    输出: 10
    :param heights: List[int]
    :return: int
    """
    """
    # 暴力O(n^2)超时
    n = len(heights)
    l_min = [float("inf")] * n
    for i in range(n):
        l_min[i] = min(heights[i], l_min[i])
    ans = 0
    for i in range(n):
        cur_min = heights[i]
        for j in range(i, n):
            if heights[j] < cur_min:
                cur_min = heights[j]
            cur = (j - i + 1) * cur_min
            if cur > ans:
                ans = cur
    return ans
    """
    """
    # 单调栈
    heights.append(0)
    stk = []
    ans = 0
    for i in range(len(heights)):
        while stk and heights[i] < heights[stk[-1]]:
            x = stk.pop()
            width = i if not stk else i - stk[-1] - 1
            ans = max(ans, heights[x] * width)
        stk.append(i)
    # print(ans)
    return ans
    """
    # 分治
    def helper(l, r):
        if l == r: return heights[l]
        m, flag = l, True
        for i in range(l+1, r+1):
            if heights[i] < heights[i - 1]:
                flag = False
            if heights[i] < heights[m]:
                m = i
        if flag:
            cur = 0
            for i in range(l, r + 1):
                cur = max(cur, heights[i] * (r - i + 1))
            return cur
        left = 0 if m == l else helper(l, m - 1)
        right = 0 if m == r else helper(m + 1, r)
        cur = heights[m] * (r - l + 1)
        return max(left, right, cur)
    n = len(heights)
    if n == 0: return 0
    return helper(0, n-1)


def insert(intervals, newInterval):
    """
    57. 插入区间
    给出一个无重叠的 ，按照区间起始端点排序的区间列表。
    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
    示例 1:
    输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出: [[1,5],[6,9]]
    示例 2:
    输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出: [[1,2],[3,10],[12,16]]
    解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
    :param intervals: List[List[int]]
    :param newInterval: List[int]
    :return: List[List[int]]
    """
    intervals = [[1,5]]
    newInterval = [0,0]

    n = len(intervals)
    res = []
    i = 0
    x, y = newInterval
    while i < n and intervals[i][1] < x:
        res.append(intervals[i])
        i += 1
    if i == n:
        res.append(newInterval)
        return res
    while i < n and intervals[i][0] <= y:
        cur = [min(intervals[i][0], x), max(intervals[i][1], y)]
        if res:
            if res[-1][1] < intervals[i][0]:
                res.append(cur)
            else:
                res[-1] = [res[-1][0], max(intervals[i][1], y)]
        else:
            res.append(cur)
        i += 1
    if not res or res[-1][1] < x:
        res.append(newInterval)
    while i < n and intervals[i][0] > y:
        res.append(intervals[i])
        i += 1
    print(res)
    return res


def countSmaller(nums):
    """
    315. 计算右侧小于当前元素的个数
    给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
    示例:
    输入: [5,2,6,1]
    输出: [2,1,1,0]
    解释:
    5 的右侧有 2 个更小的元素 (2 和 1).
    2 的右侧仅有 1 个更小的元素 (1).
    6 的右侧有 1 个更小的元素 (1).
    1 的右侧有 0 个更小的元素.
    :param nums: List[int]
    :return: List[int]
    """
    # 倒序遍历 + 二分查找 + 栈
    def binary_search_append(x):
        n = len(stk)
        i, j = 0, n - 1
        if not stk or nums[stk[-1]] >= nums[x]:
            stk.append(x)
            j += 1
        else:
            while i < j:
                mid = i + (j - i >> 1)
                if nums[stk[mid]] < nums[x]:
                    j = mid
                else:
                    i = mid + 1
            stk.insert(j, x)
        res[x] = n - j

    n = len(nums)
    res = [0] * n
    stk = []
    for i in range(n-1,-1,-1):
        binary_search_append(i)
    print(stk)
    print(res)
    return res


def findRepeatedDnaSequences(s):
    """
    187. 重复的DNA序列
    所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
    编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
    示例:
    输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出: ["AAAAACCCCC", "CCCCCAAAAA"]
    :param s: str
    :return: List[str]
    """
    window = 10
    n = len(s)
    if n < window:
        return []
    res = []
    d = {}
    for i in range(n - window + 1):
        j = i + window
        cur = s[i:j]
        d[cur] = d.get(cur, 0) + 1
        if d[cur] == 2:
            res.append(cur)
    return res


def partition(s):
    """
    131. 分割回文串
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回 s 所有可能的分割方案。
    示例:
    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
    :param s: str
    :return: List[List[str]
    """
    """
    # dfs 回溯 40%
    n = len(s)
    if n == 0: return []
    if n == 1: return [[s]]
    def dfs(i):
        if i == n - 1: return [[s[i]]]
        cur = []
        if s[i:] == s[i:][::-1]: cur.append([s[i:]])
        for j in range(i + 1, n):
            if s[i:j] == s[i:j][::-1]:
                for x in dfs(j):
                    if not [s[i:j]] + x in cur:
                        cur.append([s[i:j]] + x)
        return cur
    res = dfs(0)
    return res
    """
    # 优化: 事先将以s[i]为开头的字符串的所有回文串截止位计算出来存入g[i], 避免重复计算 98%
    n = len(s)
    g = [[] for _ in range(n)]
    for i in range(n):
        for k in range(0, min(n - i, i + 1)):
            if s[i + k] != s[i - k]:
                break
            g[i - k].append(2 * k + 1)
        for k in range(1, min(n - i, i + 2)):
            if s[i + k] != s[i - k + 1]:
                break
            g[i - k + 1].append(2 * k)
    res = []
    tmp = []
    print(g)
    def dfs(i):
        if i == n:
            res.append(tmp[:])
            return
        for x in g[i]:
            tmp.append(s[i: i + x])
            dfs(i + x)
            tmp.pop()
    dfs(0)
    return res


def recoverTree(root):
    """
    99. 恢复二叉搜索树
    二叉搜索树中的两个节点被错误地交换。
    请在不改变其结构的情况下，恢复这棵树。
    示例 1:
    输入: [1,3,null,null,2]
       1
      /
     3
      \
       2
    输出: [3,1,null,null,2]
       3
      /
     1
      \
       2
    示例 2:
    输入: [3,1,4,null,null,2]
      3
     / \
    1   4
       /
      2
    输出: [2,1,4,null,null,3]
      2
     / \
    1   4
       /
      3
    进阶:
    使用 O(n) 空间复杂度的解法很容易实现。
    你能想出一个只使用常数空间的解决方案吗？
    :param root: TreeNode
    :return: None
    """
    if root:
        stk = [root]
        res = [root.val]
        while stk:
            cur = stk.pop()
            if cur.left:
                stk.append(cur.left)
                res.append(cur.left.val)
            else:
                res.append(null)
            if cur.right:
                stk.append(cur.right)
                res.append(cur.right.val)
            else:
                res.append(null)
        print(res)


def rightSideView(root):
    """
    199. 二叉树的右视图
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    示例:
    输入: [1,2,3,null,5,null,4]
    输出: [1, 3, 4]
    解释:
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    :param root: TreeNode
    :return: List[int]
    """
    pass


if __name__ == '__main__':
    x = construct_tree_node([1,3,null,null,2])
    recoverTree(x)
    # r = partition("ababa")
    # print(r)
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # findRepeatedDnaSequences(s)
    # countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
    # insert([[1,3], [6,9]],[2,5])
    # print(largestRectangleArea([2,1,4,5,1,3,3]))
    # maximalRectangle([
    #   ["1","0","1","0","0"],
    #   ["1","0","1","1","1"],
    #   ["1","1","1","1","1"],
    #   ["1","0","0","1","0"]
    # ])
    # print(isNumber("95a54e53"))
    # simplifyPath("/a//b////c/d//././/..")
    # board = [["C","A","A"],
    #          ["A","A","A"],
    #          ["B","C","D"]]
    # print(exist(board,"AAB"))
    # x = [[0,1,2,0],
    #      [3,4,5,2],
    #      [1,3,1,5]]
    # setZeroes(x)
    # x = construct_tree_node([3,9,20,None,None,15,7])
    # levelOrder(x)
    # print(canCompleteCircuit([3,3,4],[3,4,4]))
    pass