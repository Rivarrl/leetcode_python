# -*- coding: utf-8 -*-
# ======================================
# @File    : nm4.py
# @Time    : 2019/10/24 16:32
# @Author  : Rivarrl
# ======================================
from typing import List

from algorithm_utils import *

def numRollsToTarget(d: int, f: int, target: int) -> int:
    """
    1155. 掷骰子的N种方法
    这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
    我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
    如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。
    示例 1：
    输入：d = 1, f = 6, target = 3
    输出：1
    示例 2：
    输入：d = 2, f = 6, target = 7
    输出：6
    示例 3：
    输入：d = 2, f = 5, target = 10
    输出：1
    示例 4：
    输入：d = 1, f = 2, target = 3
    输出：0
    示例 5：
    输入：d = 30, f = 30, target = 500
    输出：222616187
    提示：
    1 <= d, f <= 30
    1 <= target <= 1000
    """
    if d * f < target: return 0
    mod = 10 ** 9 + 7
    dp = [[0] * (max(f, target)+1) for _ in range(d+1)]
    for i in range(1, f+1):
        dp[1][i] = 1
    for i in range(1, d):
        for j in range(i, target):
            for k in range(1, f+1):
                if j + k <= target:
                    dp[i+1][j+k] += dp[i][j]
    return dp[d][target] % mod


def dieSimulator(n: int, rollMax: List[int]) -> int:
    """
    1223. 掷骰子模拟
    有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
    不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
    现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
    假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
    示例 1：
    输入：n = 2, rollMax = [1,1,2,2,2,3]
    输出：34
    解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
    示例 2：
    输入：n = 2, rollMax = [1,1,1,1,1,1]
    输出：30
    示例 3：
    输入：n = 3, rollMax = [1,1,1,2,2,3]
    输出：181
    提示：
    1 <= n <= 5000
    rollMax.length == 6
    1 <= rollMax[i] <= 15
    """
    dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
    mod = 10 ** 9 + 7
    for j in range(6):
        dp[1][j][0] = dp[1][j][1] = 1
    for i in range(2, n+1):
        for j in range(6):
            g = min(i, rollMax[j])
            dp[i][j][1] = sum(dp[i-1][x][0] for x in range(6) if x != j) % mod
            for k in range(2, g+1):
                dp[i][j][k] = dp[i-1][j][k-1]
            dp[i][j][0] = sum(dp[i][j][x] for x in range(1, g+1)) % mod
    res = sum(dp[n][j][0] for j in range(6))
    print(res)
    return res % mod


def reorderList(head: ListNode) -> None:
    """
    143. 重排链表
    给定一个单链表 L：L0->L1->...->Ln-1->Ln ，
    将其重新排列后变为： L0->Ln->L1->Ln-1->L2->Ln-2->...
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    示例 1:
    给定链表 1->2->3->4, 重新排列为 1->4->2->3.
    示例 2:
    给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
    """
    if not head or not head.next: return
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    p, q = slow.next, None
    while p:
        tmp = p.next
        p.next = q
        q = p
        p = tmp
    p = head
    slow.next = None
    while q:
        tmp = q.next
        q.next = p.next
        p.next = q
        p = p.next.next
        q = tmp


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    127. 单词接龙
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:
    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    输出: 5
    解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
         返回它的长度 5。
    示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    输出: 0
    解释: endWord "cog" 不在字典中，所以无法进行转换。
    """
    """
    # 一般的bfs，每次计算字符距离的话会超时，需要先把所有距离为1的单词汇总存到字典中
    from collections import defaultdict
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    d = defaultdict(list)
    l = len(beginWord)
    for w in wordList:
        for i in range(l):
            d[w[:i] + '*' + w[i+1:]].append(w)
    vis = set()
    stk = [(beginWord, 1)]
    while stk:
        word, step = stk.pop()
        for i in range(l):
            c = word[:i] + '*' + word[i + 1:]
            if endWord in d[c]: return step + 1
            for e in d[c]:
                if not e in vis:
                    stk.insert(0, (e, step+1))
                    vis.add(e)
    return 0
    """
    # 上面解法的基础上，双向bfs加速
    from collections import defaultdict
    def visit(stk, vis, vis_other):
        word, step = stk.pop()
        for i in range(l):
            c = word[:i] + '*' + word[i + 1:]
            for e in d[c]:
                if e in vis_other:
                    return step + vis_other[e]
                if not e in vis:
                    vis[e] = step + 1
                    stk.insert(0, (e, step+1))

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    d = defaultdict(list)
    l = len(beginWord)
    for w in wordList:
        for i in range(l):
            d[w[:i] + '*' + w[i+1:]].append(w)
    stk_start = [(beginWord, 1)]
    stk_end = [(endWord, 1)]
    vis_start = {beginWord: 1}
    vis_end = {endWord: 1}
    while stk_start and stk_end:
        res = visit(stk_start, vis_start, vis_end)
        if res: return res
        res = visit(stk_end, vis_end, vis_start)
        if res: return res
    return 0


def nthPersonGetsNthSeat(n: int) -> float:
    """
    1227. 飞机座位分配概率
    有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
    剩下的乘客将会：
    如果他们自己的座位还空着，就坐到自己的座位上，
    当他们自己的座位被占用时，随机选择其他座位
    第 n 位乘客坐在自己的座位上的概率是多少？
    示例 1：
    输入：n = 1
    输出：1.00000
    解释：第一个人只会坐在自己的位置上。
    示例 2：
    输入: n = 2
    输出: 0.50000
    解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
    提示：
    1 <= n <= 10^5
    """
    return 1.0 if n == 1 else 0.5


def solve(board: List[List[str]]) -> None:
    """
    130. 被围绕的区域
    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
    示例:
    X X X X
    X O O X
    X X O X
    X O X X
    运行你的函数后，矩阵变为：
    X X X X
    X X X X
    X X X X
    X O X X
    解释:
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
    """
    # 先在边缘dfs找O记录，再遍历把不在记录中的O改为X
    def dfs(i, j):
        if board[i][j] == 'X': return
        memo.add((i, j))
        for dx, dy in axis:
            x, y = i + dx, j + dy
            if x < 0 or x == n or y < 0 or y == m or (x, y) in memo: continue
            dfs(x, y)

    n = len(board)
    if n == 0: return
    m = len(board[0])
    memo = set()
    axis = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for i in range(n):
        for j in (0, m-1):
            if not (i, j) in memo:
                dfs(i, j)
    for j in range(m):
        for i in (0, n-1):
            if not (i, j) in memo:
                dfs(i, j)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O' and not (i, j) in memo:
                board[i][j] = 'X'
    matrix_pretty_print(board)


def insertionSortList(head: ListNode) -> ListNode:
    """
    147. 对链表进行插入排序
    对链表进行插入排序。
    插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
    每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
    插入排序算法：
    插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    重复直到所有输入数据插入完为止。
    示例 1：
    输入: 4->2->1->3
    输出: 1->2->3->4
    示例 2：
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
    """
    if not head or not head.next: return head
    p, pre = head.next, head
    while p:
        last, t, q = None, head, p.next
        while t and t.val < p.val:
             last, t = t, t.next
        if t != p:
            if last:
                p.next, last.next, pre.next = last.next, p, q
            else:
                p.next, head, pre.next = head, p, q
        else:
            pre = p
        p = q
    return head


def circularPermutation(n: int, start: int) -> List[int]:
    """
    5239. 循环码排列
    给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：
    p[0] = start
    p[i] 和 p[i+1] 的二进制表示形式只有一位不同
    p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
    示例 1：
    输入：n = 2, start = 3
    输出：[3,2,0,1]
    解释：这个排列的二进制表示是 (11,10,00,01)
         所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
    示例 2：
    输出：n = 3, start = 2
    输出：[2,6,7,5,4,0,1,3]
    解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
    提示：
    1 <= n <= 16
    0 <= start < 2^n
    """
    res = ['0', '1']
    for i in range(2, n+1):
        tmp = ['0' + e for e in res] + ['1' + e for e in res[::-1]]
        res = tmp
    res = [int('0b' + e, 2) for e in res]
    s = res.index(start)
    return res[s:] + res[:s]


def maxLength(arr: List[str]) -> int:
    """
    5240. 串联字符串的最大长度
    给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
    请返回所有可行解 s 中最长长度。
    示例 1：
    输入：arr = ["un","iq","ue"]
    输出：4
    解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
    示例 2：
    输入：arr = ["cha","r","act","ers"]
    输出：6
    解释：可能的解答有 "chaers" 和 "acters"。
    示例 3：
    输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
    输出：26
    提示：
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] 中只含有小写英文字母
    """
    def helper(i, c):
        if i == len(arr): return bin(c).count('1')
        res = helper(i+1, c)
        for s in arr[i]:
            d = ord(s) - ord('a')
            if c & (1 << d):
                return res
        for s in arr[i]:
            d = ord(s) - ord('a')
            c |= 1 << d
        return max(res, helper(i+1, c))
    arr = [e for e in arr if len(set(e)) == len(e)]
    if len(arr) == 0: return 0
    return helper(0, 0)


def cloneGraph(node: NeighborNode) -> NeighborNode:
    """
    133. 克隆图
    给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。
    示例：
    输入：
    {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
    解释：
    节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
    节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
    节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
    节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
    提示：
    节点数介于 1 到 100 之间。
    无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
    由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
    必须将给定节点的拷贝作为对克隆图的引用返回。
    """
    """
    # bfs
    stk = [node]
    d = {}
    while stk:
        p = stk.pop()
        q = NeighborNode(p.val, [])
        d[p] = q
        for t in p.neighbors:
            if not t in d:
                stk.insert(0, t)
    for k, v in d.items():
        for q in k.neighbors:
            v.neighbors.append(d[q])
    return d[node]
    """
    # dfs
    d = {}
    def dfs(node):
        if node in d: return d[node]
        q = NeighborNode(node.val, [])
        d[node] = q
        for t in node.neighbors:
            q.neighbors.append(dfs(t))
        return q
    return dfs(node)


if __name__ == '__main__':
    n1 = NeighborNode(1, None)
    n2 = NeighborNode(2, None)
    n3 = NeighborNode(3, None)
    n4 = NeighborNode(4, None)
    n1.neighbors, n2.neighbors, n3.neighbors, n4.neighbors = [n2, n4], [n1, n3], [n2, n4], [n1, n3]
    cloneGraph(n1)
    # r = circularPermutation(3, 2)
    # print(r)
    # r = maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"])
    # print(r)
    # x = construct_list_node([4,2,1,3])
    # y = insertionSortList(x)
    # print_list_node(y)
    # solve([["O","X","X","O","X"], ["X","O","O","X","O"], ["X","O","X","O","X"], ["O","X","O","O","O"], ["X","X","O","X","O"]])
    # x = ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    # print(x)
    # x = construct_list_node([1,2,3,4,5])
    # reorderList(x)
    # dieSimulator(3, [1,1,1,2,2,3])
    # x = numRollsToTarget(30,30,500)
    # print(x)
    pass