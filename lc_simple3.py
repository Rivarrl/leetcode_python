# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 简单题 3

def containsNearbyDuplicate(nums, k):
    """
    219. 存在重复元素 II
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
    示例 1:
    输入: nums = [1,2,3,1], k = 3
    输出: true
    示例 2:
    输入: nums = [1,0,1,1], k = 1
    输出: true
    示例 3:
    输入: nums = [1,2,3,1,2,3], k = 2
    输出: false
    :param nums: List[int]
    :param k: int
    :return: bool
    """
    l = len(nums)
    if l == 0: return False
    if l <= k: k = l - 1
    d = {}
    for i in range(k):
        d[nums[i]] = i
    for i in range(k, l):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        d[nums[i]] = i
    return False


def firstBadVersion(n):
    """
    278. 第一个错误的版本
    你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
    假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
    你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
    示例:
    给定 n = 5，并且 version = 4 是第一个错误的版本。
    调用 isBadVersion(3) -> false
    调用 isBadVersion(5) -> true
    调用 isBadVersion(4) -> true
    所以，4 是第一个错误的版本。
    :param n: int
    :return: int
    """
    def isBadVersion(x):
        pass
    i, j = 1, n
    while i < j:
        m = (i + j) >> 1
        if isBadVersion(m):
            j = m
        else:
            i = m + 1
    return i


def wordPattern(pattern, str):
    """
    290. 单词模式
    给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
    这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
    示例1:
    输入: pattern = "abba", str = "dog cat cat dog"
    输出: true
    示例 2:
    输入:pattern = "abba", str = "dog cat cat fish"
    输出: false
    示例 3:
    输入: pattern = "aaaa", str = "dog cat cat dog"
    输出: false
    示例 4:
    输入: pattern = "abba", str = "dog dog dog dog"
    输出: false
    说明:
    你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
    :param pattern: str
    :param str: str
    :return: bool
    """
    alist = str.split(' ')
    l = len(alist)
    if l != len(pattern) or len(set(alist)) != len(set([x for x in pattern])): return False
    d = {}
    for i in range(l):
        if not pattern[i] in d:
            d[pattern[i]] = alist[i]
        else:
            if d[pattern[i]] != alist[i]:
                return False
    return True


def moveZeroes(nums):
    """
    283. 移动零
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
    说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
    :param nums: List[int]
    :return: None
    """
    l = len(nums)
    i, j = 0, 0
    while i < l:
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
        i += 1
    while j < l:
        nums[j] = 0
        j += 1
    print(nums)


def isPalindrome(head):
    """
    234. 回文链表
    请判断一个链表是否为回文链表。
    示例 1:
    输入: 1->2
    输出: false
    示例 2:
    输入: 1->2->2->1
    输出: true
    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
    :param head: ListNode
    :return: bool
    """
    """
    # 用了栈，O(n)空间
    if not head: return True
    p, q = head, head
    l = 1
    while p.next and q.next and q.next.next:
        p = p.next
        q = q.next.next
        l += 1
    stk = []
    if q.next:
        p = p.next
    for _ in range(l):
        stk.append(p)
        p = p.next
    while stk:
        if head.val != stk.pop().val:
            return False
        head = head.next
    return True
    """
    # O(1) 空间
    if not head: return True
    slow, fast = head, head
    while fast:
        slow = slow.next
        fast = None if not fast.next else fast.next.next
    daeh = None
    while slow:
        daeh, slow.next, slow = slow, daeh, slow.next
    while head and daeh:
        if head.val != daeh.val:
            return False
        head = head.next
        daeh = daeh.next
    return True


def binaryTreePaths(root):
    """
    257. 二叉树的所有路径
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    输入:
       1
     /   \
    2     3
     \
      5
    输出: ["1->2->5", "1->3"]
    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
    :param root: TreeNode
    :return: List[str]
    """
    """
    # 回溯
    res = []
    if root:
        if not root.left and not root.right:
            res.append("{}".format(root.val))
        else:
            for i in binaryTreePaths(root.left):
                res.append("{}->{}".format(root.val, i))
            for i in binaryTreePaths(root.right):
                res.append("{}->{}".format(root.val, i))
    return res
    """
    # dfs
    def dfs(root, cur, res):
        if not root.left and not root.right:
            cur = "%s%d"%(cur, root.val)
            res.append(cur)
        else:
            cur = "%s%d->"%(cur, root.val)
            if root.left:
                dfs(root.left, cur, res)
            if root.right:
                dfs(root.right, cur, res)
    res = []
    if root:
        dfs(root, "", res)
    return res


def sumOfLeftLeaves(root):
    """
    404. 左叶子之和
    计算给定二叉树的所有左叶子之和。
    示例：
        3
       / \
      9  20
        /  \
       15   7
    在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
    :param root: TreeNode
    :return: int
    """
    def helper(root, isl):
        if root:
            if not root.left and not root.right and isl:
                ans[-1] += root.val
            if root.left:
                helper(root.left, True)
            if root.right:
                helper(root.right, False)
    ans = [0]
    helper(root, False)
    return ans[-1]


def findNthDigit(n):
    """
    400. 第N个数字
    在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
    注意:
    n 是正数且在32为整形范围内 ( n < 231)。
    示例 1:
    输入:
    3
    输出:
    3
    示例 2:
    输入:
    11
    输出:
    0
    说明:
    第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
    :param n: int
    :return: int
    """
    x, i, t = 0, 0, 0
    while n > x:
        i += 1
        t, x = x, x + i * 9 * 10 ** (i - 1)
    n -= (t + 1)
    # print(n)
    # print((10**(i-1)) + (n // i))
    # print((n % i))
    # print(str((10**(i-1)) + (n // i))[n % i])
    return int(str((10**(i-1)) + (n // i))[n % i])


def shortestToChar(S, C):
    """
    821. 字符的最短距离
    给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
    示例 1:
    输入: S = "loveleetcode", C = 'e'
    输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    说明:
    字符串 S 的长度范围为 [1, 10000]。
    C 是一个单字符，且保证是字符串 S 里的字符。
    S 和 C 中的所有字母均为小写字母。
    :param S: str
    :param C: str
    :return: List[int]
    """
    n = len(S)
    res = [n] * n
    for i in range(n):
        if S[i] == C:
            res[i] = 0
        else:
            if i > 0 and res[i-1] < n:
                res[i] = res[i-1] + 1
    for j in range(n-1, -1, -1):
        if j < n-1:
            res[j] = min(res[j+1] + 1, res[j])
    return res


def findDisappearedNumbers(nums):
    """
    448. 找到所有数组中消失的数字
    给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。
    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
    示例:
    输入:
    [4,3,2,7,8,2,3,1]
    输出:
    [5,6]
    :param nums: List[int]
    :return: List[int]
    """
    """
    # 座位交换法
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    res = []
    for i in range(n):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res
    """
    # 置负值法
    n = len(nums)
    for i in range(n):
        nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
    res = []
    for i in range(n):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res


if __name__ == '__main__':
    pass
    findDisappearedNumbers([4,3,2,7,8,2,3,1])
    # findNthDigit(10)
    # x = construct_tree_node([1,2,3,None,5])
    # print(binaryTreePaths(x))
    # x = construct_list_node([1,2])
    # print(isPalindrome(x))
    # moveZeroes([0,1,0,3,13])
    # print(containsNearbyDuplicate([1,2,3,1,2,3], 2))