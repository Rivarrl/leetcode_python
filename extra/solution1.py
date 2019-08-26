import random
import time
from algorithm_utils import *


def question1(arr):
    """
    数字键盘按键
    1234567890
    操作有：按下、左移和右移
    初始左右手分别在5和6的位置，问敲出给定序列的最小操作次数
    :param arr: List[int]
    :return: int
    """
    """
    # dfs + 剪枝 感觉还是会超时
    def dfs(i, j, k, cur):
        nonlocal ans
        if cur >= ans: return
        if k == n:
            ans = min(ans, cur)
            return
        arr[k] = arr[k] + 10 if arr[k] == 0 else arr[k]
        if arr[k] >= j:
            dfs(i, arr[k], k + 1, cur + arr[k] - j)
        elif arr[k] <= i:
            dfs(arr[k], j, k + 1, cur + i - arr[k])
        else:
            dfs(i, arr[k], k + 1, cur + j - arr[k])
            dfs(arr[k], j, k + 1, cur + arr[k] - i)

    n = len(arr)
    ans = float("inf")
    dfs(5, 6, 0, n)
    print(ans)
    return ans
    """
    # dfs + memo
    def dfs(i, j, k, cur):
        if k == n or cur > memo[k][i][j]:
            return
        memo[k][i][j] = cur
        arr[k] = arr[k] + 10 if arr[k] == 0 else arr[k]
        if arr[k] >= j:
            dfs(i, arr[k], k + 1, cur + arr[k] - j)
        elif arr[k] <= i:
            dfs(arr[k], j, k + 1, cur + i - arr[k])
        else:
            dfs(i, arr[k], k + 1, cur + j - arr[k])
            dfs(arr[k], j, k + 1, cur + arr[k] - i)

    n = len(arr)
    inf = float("inf")
    # 保存某状态的最优解 memo[k][i][j]表示第k次操作两只手在i和j时的最小操作次数
    memo = [[[inf] * 10 for _ in range(11)] for _ in range(n)]
    x, y = 5, 6
    dfs(x, y, 0, n)
    if n == 1:
        x = arr[-1]
    elif n >= 2:
        x, y = arr[-2], arr[-1]
    if x > y:
        x, y = y, x
    print(memo[n-1][x][y])
    return memo[n-1][x][y]


def question2(arr):
    """
    交换产生最大的数
    如：1,3,2 -> 3,1,2
    4, 6, 7, 1 -> 7, 6, 4, 1
    :param arr: List[int]
    :return: List[int]
    """
    a = arr[:]
    print(a)
    N = len(arr)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(i):
        left = i * 2 + 1
        right = left + 1
        root = i
        if left < N and arr[left] > arr[root]:
            root = left
        if right < N and arr[right] > arr[root]:
            root = right
        if root != i:
            swap(arr, i, root)
            heapify(root)

    for i in range(len(arr) // 2, -1, -1):
        heapify(i)

    j = 0
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, i, 0)
        if a[j] != arr[i]:
            k = a.index(arr[i])
            swap(a, k, j)
            break
        N -= 1
        j += 1
        heapify(0)
    print(a)
    return a

def question3(root):
    """
    二叉搜索树转排序双向链表
    :param root: TreeNode
    :return: TreeNode
    """
    def helper(node):
        if node and node.left:
            helper(node.left)
        nonlocal last
        p = node
        p.left = last
        if last: last.right = p
        last = p
        if node.right:
            helper(node.right)
    last = None
    helper(root)
    while last and last.left:
        last = last.left
    return last


def jd_dev1(nums):
    """
    合唱队排序最多分组（京东2019秋招开发岗）
    合唱队的N名学生站成一排且从左到右编号为1到N，其中编号为i的学生身高为H(i).
    现在将这些学生分成若干组（同一组的学生编号连续），并让每组学生从左到右按身高从低到高进行排列
    使得最后所有学生同样满足从左到右身高从低到高（中间位置可以等高）
    问：那么最多能将这些学生分成多少组？
    例如：
    输入：2 1 3 2
    结果：2
    :param nums: List[int]
    :return: int
    """
    def dfs(nums, l, r):
        if l > r: return 0
        if l == r: return 1
        if dp[l][r] > 0:
            return dp[l][r]
        mi, ma = float('inf'), -float('inf')
        rmi, rma = 0, 0
        for i in range(l, r+1):
            if nums[i] <= mi:
                mi = nums[i]
                rmi = i
        for i in range(r, l-1, -1):
            if nums[i] >= ma:
                ma = nums[i]
                rma = i
        if rmi >= rma:
            ans = 1
            for i in range(l, r+1):
                if nums[i] == mi:
                    ans += 1
                else:
                    break
            for i in range(r, l-1, -1):
                if nums[i] == ma:
                    ans += 1
                else:
                    break
        else:
            ans = 2 + dfs(nums, rmi + 1, rma - 1)
        dp[l][r] = ans
        return ans

    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    ans = dfs(nums, 0, n-1)
    print(dp)
    print(ans)
    return ans


def jd_alg1(unit):
    """
    拼接迷宫（2019京东秋招算法岗笔试题1）
    构造一个迷宫是很麻烦的一件事情，因此有人提出来一种迷宫生成方法，与铺砖的方法类似
    首先设计一个n*m的单位迷宫，然后就想铺砖一样，将这个单位迷宫复制拼接起来
    如果能够通过这种方式生成的迷宫可以从起始位置通向无穷多的位置，那么我们认为这个单位迷宫是合法的（每个单位不可旋转）
    单位迷宫的表示包含三种符号，'#', '.'和'S', 其中'#'代表墙，'.'代表没有障碍物可以通过，S则代表的是起始位置
    迷宫只有一个起点，可以任选一个单位迷宫的S位置作为起点，其他单位迷宫的S则视为可通行的
    问：输入的单位迷宫是否合法，是返回'Yes'，否则返回'No'
    例如：
    输入：[['S', '#'], ['#', '.']]
    输出：No
    :param unit: List[List[str]]
    :return: str
    """


def jd_alg2(board):
    """
    消消乐（2019京东秋招算法岗笔试题2）
    游戏棋盘大小为5*5的正方形网格，每个格子中有一个大于0且小于4的整数
    对于一个确定的局面，若一个各自与它上下左右四个方向的各自（如果存在）数字相同，则称这两个格子是连通的，并且这种连通具有传递性
    每次，有你可以选择一个格子，若于这个格子连通的格子（包括自己）数大于等于3，你就可以选择消掉这个各自，与此同时，与这个格子连通
    的所有格子会一起消失。
    消消乐的另一个特性是重力系统，每次消掉某个格子之后，网格中保留的一些数字会失去支撑而下落
    问：怎样玩才能使得最后剩下的不能消掉的格子尽量少
    例如：
    输入：[[3,1,2,1,1],[1,1,1,1,3],[1,1,1,1,1],[1,1,1,1,1],[3,1,2,2,2]]
    输出：[[0, 1],[3, 2]]
    解释：
    31211  3x2xx  xxxxx  xxxxx  xxxxx
    11113  xxxx3  xxxxx  xxxxx  xxxxx
    11111  xxxxx  xxxxx  xxxxx  xxxxx
    11111  xxxxx  3x2x3  3xxx3  3xxxx
    31222  3x222  3x222  3xxxx  3xxx3
    x表示空缺，每个连通块用相同的颜色标记，此过程演示样例
    :param board: List[List[int]]
    :return: List[int]
    """


def yfd_dev2(group):
    """
    分组讨论（2019猿辅导秋招笔试题2）
    猿辅导要实现一个分组讨论的功能，要求每个学生选好自己的组别，然后在任意三组中抽取一位学生组成新的讨论组
    问：给定每个组的人数，最多可以分多少组
    例如：
    输入：[1,2,1]
    输出: 1
    :param group: List[int]
    :return: int
    """
    # 使用最大堆，由于heapq是支持最小堆，所以用相反数来实现最大堆
    import heapq
    max_heap = []
    for g in group:
        if g > 0:
            heapq.heappush(max_heap, -g)
    ans = 0
    while len(max_heap) >= 3:
        large = []
        for i in range(3):
            large.append(heapq.heappop(max_heap))
        large[0] -= large[2]
        large[1] -= large[2]
        ans -= large[2]
        for lg in large[:-1]:
            if lg < 0:
                heapq.heappush(max_heap, lg)
    print(ans)
    return ans


def yfd_dev3(ori, dest, k, step):
    """
    打字机（猿辅导2019秋招笔试题3）
    有一台只能打出ABC三个字母的打字机
    规定一次操作为：变换k个字符至可以打的其他字符（例如：k=2时，AA -> BC(ABC中任意两个不是A的字符)）
    问：给定原字符串和目标字符串，变换操作次数k和变换次数n，有多少种变换？结果超出10^9+7取mod
    例如：
    输入：ori='AAA', dest='CCC', k = 3, step = 2
    输出：1
    解释：k=3，n=2时只有AAA -> BBB -> CCC一种变换方法
    :param ori: str
    :param dest: str
    :param k: int
    :param step: int
    :return: int
    """
    # n = len(ori)
    # dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(step+1)]
    # a, b = ori.count('A'), ori.count('B')
    # dp[a][b][0] = 1
    def dfs(c, d, s):
        if s > step: return 0
        if s == step:
            if c == d:
                return 1
            else:
                return 0


def bd_alg1(n):
    """
    花园修路（字节跳动2019秋招算法岗笔试题1）
    现有一个圆形花园共有n个入口，现在要修一些路，穿过这些花园。要求每个入口只能有一条路，所有的路均不会相交。
    求所有可行的方法总数 (n为2~1000的偶数), 结果超过10^9+7取mod
    :param n: int
    :return: int
    """
    dp = [0] * (n//2 + 1)
    dp[1] = 1
    for i in range(2, n//2+1):
        dp[i] = (dp[i-1] + 3**(i-2)) % (10**9+7)
    print(dp)
    return dp[n//2]


if __name__ == '__main__':
    bd_alg1(8)
    # yfd_dev2([0,2,4,99])
    # jd_dev1([1,3,2,6,5,4,7,8,10,9])
    # x = construct_tree_node([4,2,6,1,3,5,7])
    # question3(x)
    # question1([6,9,7,1,7])
    # question2([8, 7, 6, 5, 4, 2, 3, 1])
    pass
