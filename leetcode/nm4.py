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
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是"相连"的。
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


def findMin(nums: List[int]) -> int:
    """
    153. 寻找旋转排序数组中的最小值
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
    示例 1:
    输入: [3,4,5,1,2]
    输出: 1
    示例 2:
    输入: [4,5,6,7,0,1,2]
    输出: 0
    """
    i, j = 0, len(nums) - 1
    while i < j:
        m = i + (j - i) // 2
        if nums[m] > nums[j]:
            i = m + 1
        else:
            j = m
    return nums[i]


def reverseWords(s: str) -> str:
    """
    151. 翻转字符串里的单词
    给定一个字符串，逐个翻转字符串中的每个单词。
    示例 1：
    输入: "the sky is blue"
    输出: "blue is sky the"
    示例 2：
    输入: "  hello world!  "
    输出: "world! hello"
    解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    示例 3：
    输入: "a good   example"
    输出: "example good a"
    解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
    说明：
    无空格字符构成一个单词。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
    进阶：
    请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
    """
    # 一行
    # return ' '.join([e for e in s.strip().split(' ') if e][::-1])
    # 伪O(1)空间思路, 反向遍历，双指针停留到每个单词的首尾再向中心做交换
    chars = [c for c in s.strip()]
    i, j, n = 0, 0, len(chars)
    while j < n:
        if (chars[j] == ' ' or j == n - 1) and chars[i] != ' ':
            k = j - int(chars[j] == ' ')
            while i < k:
                swap(chars, i, k)
                i += 1
                k -= 1
            i = j
        elif chars[i] == ' ' and chars[j] != ' ':
            i = j
        j += 1
    for i in range(n//2):
        j = n - 1 - i
        swap(chars, i, j)
    e = 0
    for i in range(1, n):
        if e > 0 and chars[i] != ' ':
            swap(chars, i, i-e)
        elif chars[i] == ' ' and chars[i-e-1] == ' ':
            e += 1
    chars = chars[:-e] if e else chars
    return ''.join(chars)


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    """
    1202. 交换字符串中的元素
    给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
    你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
    返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
    示例 1:
    输入：s = "dcab", pairs = [[0,3],[1,2]]
    输出："bacd"
    解释：
    交换 s[0] 和 s[3], s = "bcad"
    交换 s[1] 和 s[2], s = "bacd"
    示例 2：
    输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    输出："abcd"
    解释：
    交换 s[0] 和 s[3], s = "bcad"
    交换 s[0] 和 s[2], s = "acbd"
    交换 s[1] 和 s[2], s = "abcd"
    示例 3：
    输入：s = "cba", pairs = [[0,1],[1,2]]
    输出："abc"
    解释：
    交换 s[0] 和 s[1], s = "bca"
    交换 s[1] 和 s[2], s = "bac"
    交换 s[0] 和 s[1], s = "abc"
    提示：
    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s 中只含有小写英文字母
    """
    # 找连通分量，用union-find，相同连接中的位置的字符相对字典序最低
    from collections import defaultdict
    def find(p):
        while parent[p] != p:
            p = parent[p]
        return p

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i == root_j: return
        if sz[root_i] > sz[root_j]:
            parent[root_j] = root_i
            sz[root_i] += sz[root_j]
        else:
            parent[root_i] = root_j
            sz[root_j] += sz[root_i]

    n = len(s)
    parent = [i for i in range(n)]
    sz = [1 for _ in range(n)]
    for i, j in pairs:
        union(i, j)
    d = defaultdict(list)
    for i in range(n):
        d[find(i)].append(i)
    ls = [e for e in s]
    for v in d.values():
        tmp = sorted([ls[e] for e in v])
        for i in range(len(v)):
            ls[v[i]] = tmp[i]
    s = ''.join(ls)
    return s


def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    """
    1052. 爱生气的书店老板
    今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
    在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
    书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
    请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
    示例：
    输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
    输出：16
    解释：
    书店老板在最后 3 分钟保持冷静。
    感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
    提示：
    1 <= X <= customers.length == grumpy.length <= 20000
    0 <= customers[i] <= 1000
    0 <= grumpy[i] <= 1
    """
    n = len(customers)
    if n <= X: return sum(customers)
    res = 0
    for i in range(n):
        if i < X:
            res += customers[i]
        else:
            res += customers[i] * (grumpy[i] ^ 1)
    cur = res
    for i in range(n-X):
        j = i + X
        cur += grumpy[j] * customers[j] - grumpy[i] * customers[i]
        res = max(res, cur)
    return res


def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    """
    1201. 丑数 III
    请你帮忙设计一个程序，用来找出第 n 个丑数。
    丑数是可以被 a 或 b 或 c 整除的 正整数。
    示例 1：
    输入：n = 3, a = 2, b = 3, c = 5
    输出：4
    解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
    示例 2：
    输入：n = 4, a = 2, b = 3, c = 4
    输出：6
    解释：丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。
    示例 3：
    输入：n = 5, a = 2, b = 11, c = 13
    输出：10
    解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
    示例 4：
    输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
    输出：1999999984
    提示：
    1 <= n, a, b, c <= 10^9
    1 <= a * b * c <= 10^18
    本题结果在 [1, 2 * 10^9] 的范围内
    """
    def gcd(x, y):
        if x == 0: return y
        return gcd(y%x, x)
    ab, ac, bc = a // gcd(a, b) * b, a // gcd(a, c) * c, b // gcd(b, c) * c
    abc = ab // gcd(ab, c) * c
    mi = min(a, b, c)
    lo, hi = mi, mi * n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        m = mid // a + mid // b + mid // c - (mid // ab + mid // ac + mid // bc) + mid // abc
        if m >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def reorganizeString(S: str) -> str:
    """
    767. 重构字符串
    给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
    若可行，输出任意可行的结果。若不可行，返回空字符串。
    示例 1:
    输入: S = "aab"
    输出: "aba"
    示例 2:
    输入: S = "aaab"
    输出: ""
    注意:
    S 只包含小写字母并且长度在[1, 500]区间内。
    """
    from collections import defaultdict
    import heapq
    n = (len(S) + 1) // 2
    d = defaultdict(int)
    for c in S:
        d[c] += 1
        if d[c] > n:
            return ""
    pq = [(-v, k) for k, v in d.items()]
    heapq.heapify(pq)
    res = []
    while pq:
        v1, k1 = heapq.heappop(pq)
        res.append(k1)
        v1 += 1
        if pq:
            v2, k2 = heapq.heappop(pq)
            res.append(k2)
            v2 += 1
            if v2 < 0:
                heapq.heappush(pq, (v2, k2))
        if v1 < 0:
            heapq.heappush(pq, (v1, k1))
    return "".join(res)


@timeit
def maxRepOpt1(text: str) -> int:
    """
    1156. 单字符重复子串的最大长度
    如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
    给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
    示例 1：
    输入：text = "ababa"
    输出：3
    示例 2：
    输入：text = "aaabaaa"
    输出：6
    示例 3：
    输入：text = "aaabbaaa"
    输出：4
    示例 4：
    输入：text = "aaaaa"
    输出：5
    示例 5：
    输入：text = "abcdef"
    输出：1
    提示：
    1 <= text.length <= 20000
    text 仅由小写英文字母组成。
    """
    # 计算可以容忍一个字符不同的最长重复字符串长度，和该字符的总个数，如果不相等答案+1
    from collections import defaultdict
    d = defaultdict(list)
    i, n = 0, len(text)
    while i < n:
        j = 1
        c = text[i]
        while i + j < n and c == text[i+j]:
            j += 1
        d[c].append([j, (i, i+j)])
        i += j
    res = 0
    for k, v in d.items():
        f1, f2 = int(len(v) > 1), int(len(v) > 2)
        cur = v[len(v) - 1][0] + f1
        for i in range(len(v) - 1):
            cur = max(cur, v[i][0] + f1)
            if v[i][1][1] + 1 == v[i+1][1][0]:
                cur = max(cur, v[i][0] + v[i+1][0] + f2)
        res = max(res, cur)
    return res


def subarraySum(nums: List[int], k: int) -> int:
    """
    560. 和为K的子数组
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    示例 1 :
    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :
    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
    """
    from collections import defaultdict
    s = defaultdict(int)
    s[0] += 1
    res, c = 0, 0
    for x in nums:
        c += x
        print(c, c-k)
        res += s[c-k]
        s[c] += 1
    return res


def subarraysDivByK(A: List[int], K: int) -> int:
    """
    974. 和可被 K 整除的子数组
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    示例：
    输入：A = [4,5,0,-2,-3,1], K = 5
    输出：7
    解释：
    有 7 个子数组满足其元素之和可被 K = 5 整除：
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    提示：
    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000
    """
    from collections import defaultdict
    s = defaultdict(int)
    s[0] += 1
    res, x = 0, 0
    for a in A:
        x = (x + a) % K
        res += s[x]
        s[x] += 1
    return res


@timeit
def findSubstringInWraproundString(p: str) -> int:
    """
    467. 环绕字符串中唯一的子字符串
    把字符串 s 看作是"abcdefghijklmnopqrstuvwxyz"的无限环绕字符串，所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
    现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 
    注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。
    示例 1:
    输入: "a"
    输出: 1
    解释: 字符串 S 中只有一个"a"子字符。
    示例 2:
    输入: "cac"
    输出: 2
    解释: 字符串 S 中的字符串"cac"只有两个子串"a"、"c"。
    示例 3:
    输入: "zab"
    输出: 6
    解释: 在字符串 S 中有六个子串"z"、"a"、"b"、"za"、"ab"、"zab"。
    """
    # 记录最长连续字符串中的字母标号
    if len(p) <= 1: return len(p)
    last = ord(p[0])
    d = {p[0]: 1}
    ctr = 1
    for c in p[1:]:
        if (ord(c) - last + 26) % 26 == 1:
            ctr += 1
        else:
            ctr = 1
        d[c] = max(d.get(c, 0), ctr)
        last = ord(c)
    print(d)
    return sum(d.values())


@timeit
def maxSumAfterPartitioning(A: List[int], K: int) -> int:
    """
    1043. 分隔数组以得到最大和
    给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。
    返回给定数组完成分隔后的最大和。
    示例：
    输入：A = [1,15,7,9,2,5,10], K = 3
    输出：84
    解释：A 变为 [15,15,15,9,10,10,10]
    提示：
    1 <= K <= A.length <= 500
    0 <= A[i] <= 10^6
    """
    # 动态规划
    n = len(A)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        j = i - 1
        cur_max = float('-inf')
        while i - j <= K and j >= 0:
            cur_max = max(cur_max, A[j])
            dp[i] = max(dp[i], dp[j] + cur_max * (i-j))
            j -= 1
    return dp[n]


@timeit
def canPartition(nums: List[int]) -> bool:
    """
    416. 分割等和子集
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].
    示例 2:
    输入: [1, 2, 3, 5]
    输出: false
    解释: 数组不能分割成两个元素和相等的子集.
    """
    """
    # 自顶向下记忆化搜索
    x = sum(nums)
    if x & 1: return False
    def dfs(v, i):
        if i == 0: return v == nums[0]
        if dp[i][v] != None:
            return dp[i][v]
        dp[i][v] = dfs(v-nums[i], i-1) or dfs(v, i-1)
        return dp[i][v]

    hf = x // 2
    n = len(nums)
    dp = [[None] * (hf+1) for _ in range(n+1)]
    return dfs(hf, n-1)
    """
    # 自底向上动态规划
    n = len(nums)
    if n < 2: return False
    x = sum(nums)
    if x & 1: return False
    hf = x // 2
    dp = [[False] * (hf+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][0] = True
    if nums[0] == hf: return True
    elif nums[0] < hf:
        dp[0][nums[0]] = False
    for i in range(1, n):
        for v in range(1, hf+1):
            dp[i][v] = dp[i-1][v-nums[i]] or dp[i-1][v]
    return dp[n-1][hf]


@timeit
def wiggleMaxLength(nums: List[int]) -> int:
    """
    376. 摆动序列
    如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
    例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
    给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
    示例 1:
    输入: [1,7,4,9,2,5]
    输出: 6
    解释: 整个序列均为摆动序列。
    示例 2:
    输入: [1,17,5,10,13,15,10,5,16,8]
    输出: 7
    解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
    示例 3:
    输入: [1,2,3,4,5,6,7,8,9]
    输出: 2
    进阶:
    你能否用 O(n) 时间复杂度完成此题?
    """
    n = len(nums)
    if n == 0: return 0
    up, down = 1, 1
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
    return max(up, down)


@timeit
def checkSubarraySum(nums: List[int], k: int) -> bool:
    """
    523. 连续的子数组和
    给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
    示例 1:
    输入: [23,2,4,6,7], k = 6
    输出: True
    解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
    示例 2:
    输入: [23,2,6,4,7], k = 6
    输出: True
    解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
    说明:
    数组的长度不会超过10,000。
    你可以认为所有数字总和在 32 位有符号整数范围内。
    """
    d = {0: -1}
    c = 0
    for i, x in enumerate(nums):
        c += x
        if k != 0:
            c %= k
        print(d)
        if not c in d: d[c] = i
        elif i - d[c] > 1: return True
    return False



if __name__ == '__main__':
    checkSubarraySum([0,3,5], 3)
    # wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    # canPartition([100])
    # maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)
    # findSubstringInWraproundString("zabcefghicdefgh")
    # res = subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5)
    # print(res)
    # subarraySum([1,2,2,0,-1,5], 4)
    # res = maxRepOpt1("babbaaabbbbbaa")
    # print(res)
    # res = reorganizeString("aaaaaaabcdwcc")
    # print(res)
    # res = nthUglyNumber(4,2,3,4)
    # print(res)
    # res = maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3)
    # print(res)
    # smallestStringWithSwaps("dcab", [[0,3],[1,2]])
    # r = reverseWords("a good   example")
    # print(r)
    # ans = findMin([1,2,3])
    # print(ans)
    # n1 = NeighborNode(1, None)
    # n2 = NeighborNode(2, None)
    # n3 = NeighborNode(3, None)
    # n4 = NeighborNode(4, None)
    # n1.neighbors, n2.neighbors, n3.neighbors, n4.neighbors = [n2, n4], [n1, n3], [n2, n4], [n1, n3]
    # cloneGraph(n1)
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