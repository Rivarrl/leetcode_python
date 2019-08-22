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


if __name__ == '__main__':
    x = construct_tree_node([4,2,6,1,3,5,7])
    question3(x)
    # question1([6,9,7,1,7])
    # question2([8, 7, 6, 5, 4, 2, 3, 1])
    pass
