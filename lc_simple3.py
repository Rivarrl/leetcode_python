# -*- coding:utf-8 -*-
from algorithm_utils import *
import re

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


def pathSum(root, sum):
    """
    437. 路径总和 III
    给定一个二叉树，它的每个结点都存放着一个整数值。
    找出路径和等于给定数值的路径总数。
    路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
    二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
    示例：
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    返回 3。和等于 8 的路径有:
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3.  -3 -> 11
    :param root: TreeNode
    :param sum: int
    :return: int
    """
    """
    # 5%
    def helper(root, sum):
        ans = 0
        if root:
            left = helper(root.left, sum - root.val)
            right = helper(root.right, sum - root.val)
            ans = left + right + (root.val == sum)
        return ans
    def tree_walk(root, sum):
        if root:
            ans[0] += helper(root, sum)
            tree_walk(root.left, sum)
            tree_walk(root.right, sum)
    ans = [0]
    tree_walk(root, sum)
    return ans[0]
    """
    # 100% 用字典记录每个节点的结果
    from collections import defaultdict
    def helper(node, s):
        if not node:
            return
        s += node.val
        ans[0] += lookup[s - sum]
        lookup[s] += 1
        helper(node.left, s)
        helper(node.right, s)
        lookup[s] -= 1
    lookup = defaultdict(int)
    lookup[0] = 1
    ans = [0]
    helper(root, 0)
    return ans[0]


def isUgly(num):
    """
    263. 丑数
    编写一个程序判断给定的数是否为丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
    示例 1:
    输入: 6
    输出: true
    解释: 6 = 2 × 3
    示例 2:
    输入: 8
    输出: true
    解释: 8 = 2 × 2 × 2
    示例 3:
    输入: 14
    输出: false
    解释: 14 不是丑数，因为它包含了另外一个质因数 7。
    说明：
    1 是丑数。
    输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
    :param num: int
    :return: bool
    """
    if num <= 0: return False
    while num % 2 == 0:
        num//=2
    while num % 3 == 0:
        num//=3
    while num % 5 == 0:
        num//=5
    return num == 1


def addDigits(num):
    """
    258. 各位相加
    给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
    示例:
    输入: 38
    输出: 2
    解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
    进阶:
    你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
    :param num: int
    :return: int
    """
    """
    # 老实人循环
    while num > 9:
        p, temp = num, 0
        while p > 9:
            temp += p % 10
            p //= 10
        temp += p
        num = temp
    return num
    """
    # 找规律
    return num if num < 10 else (num - 10) % 9 + 1


def reverseVowels(s):
    """
    345. 反转字符串中的元音字母
    编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
    示例 1:
    输入: "hello"
    输出: "holle"
    示例 2:
    输入: "leetcode"
    输出: "leotcede"
    说明:
    元音字母不包含字母"y"。
    :param s: str
    :return: str
    """
    i, j = 0, len(s) - 1
    uan = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ls = [x for x in s]
    while i < j:
        while i < j and ls[i] not in uan:
            i += 1
        while i < j and ls[j] not in uan:
            j -= 1
        if i < j:
            ls[i], ls[j] = ls[j], ls[i]
        i += 1
        j -= 1
    return ''.join(ls)


def isPowerOfFour(num):
    """
    342. 4的幂
    给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
    示例 1:
    输入: 16
    输出: true
    示例 2:
    输入: 5
    输出: false
    进阶：
    你能不使用循环或者递归来完成本题吗？
    :param num: int
    :return: bool
    """
    """
    # 正则
    x = bin(num).lstrip('0b')
    return re.match("^10*$", x) is not None and x.count('0') % 2 == 0
    """
    # 位运算
    # 判断是否为2的幂
    if num < 0 or num & (num - 1):
        return False
    # 判断是否为4的幂
    # 0x5 = 0b0101, 校验奇数位是否为0
    # return num & 0x55555555
    # 所有2的幂中, 符合num % 3 == 1的就是4的幂, 如4, 16, 64, ...
    return num % 3 == 1


def canPlaceFlowers(flowerbed, n):
    """
    605. 种花问题
    假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
    给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
    示例 1:
    输入: flowerbed = [1,0,0,0,1], n = 1
    输出: True
    示例 2:
    输入: flowerbed = [1,0,0,0,1], n = 2
    输出: False
    注意:
    数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。
    :param flowerbed: List[int]
    :param n: int
    :return: bool
    """
    """
    # 迭代
    board_flowerbed = [0] + flowerbed + [0]
    size = len(board_flowerbed)
    if size == 2: return False
    for i in range(2, size):
        if n == 0: return True
        if board_flowerbed[i] == 0 and board_flowerbed[i-1] == 0 and board_flowerbed[i-2] == 0:
            board_flowerbed[i-1] = 1
            n -= 1
    return n == 0
    """
    # 递归
    def helper(i, n):
        if n == 0: return True
        while i < size and (board_flowerbed[i-2] == 1 or board_flowerbed[i-1] == 1 or board_flowerbed[i]) == 1:
            i += 1
        if i < size:
            board_flowerbed[i-1] = 1
            return helper(i, n-1)
        else:
            return False

    board_flowerbed = [0] + flowerbed + [0]
    size = len(board_flowerbed)
    return helper(2, n)


def findContentChildren(g, s):
    """
    455. 分发饼干
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
    注意：
    你可以假设胃口值为正。
    一个小朋友最多只能拥有一块饼干。
    示例 1:
    输入: [1,2,3], [1,1]
    输出: 1
    解释:
    你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
    虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
    所以你应该输出1。
    示例 2:
    输入: [1,2], [1,2,3]
    输出: 2
    解释:
    你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
    你拥有的饼干数量和尺寸都足以让所有孩子满足。
    所以你应该输出2.
    :param g: List[int]
    :param s: List[int]
    :return: int
    """
    g.sort()
    s.sort()
    gn = len(g)
    sn = len(s)
    i, j, ans = 0, 0, 0
    while i < gn and j < sn:
        if g[i] <= s[j]:
            ans += 1
            i += 1
        j += 1
    return ans


def gcdOfStrings(str1, str2):
    """
    1071. 字符串的最大公因子
    对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
    返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
    示例 1：
    输入：str1 = "ABCABC", str2 = "ABC"
    输出："ABC"
    示例 2：
    输入：str1 = "ABABAB", str2 = "ABAB"
    输出："AB"
    示例 3：
    输入：str1 = "LEET", str2 = "CODE"
    输出：""
    提示：
    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] 和 str2[i] 为大写英文字母
    :param str1: str
    :param str2: str
    :return: str
    """
    n1 = len(str1)
    n2 = len(str2)
    if n1 < n2:
        str1, str2 = str2, str1
    while str2 != "":
        tmp = str1.replace(str2, "")
        if tmp == str1:
            return ""
        str1, str2 = str2, tmp
    return str1


def merge(nums1, m, nums2, n):
    """
    88. 合并两个有序数组
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    输出: [1,2,2,3,5,6]
    :param nums1: List[int]
    :param m: int
    :param nums2: List[int]
    :param n: int
    :return: None
    """
    i, j, k = m, n, m + n
    while k > 0:
        if i == 0:
            nums1[k - 1] = nums2[j - 1]
            j -= 1
        elif j == 0:
            nums1[k - 1] = nums1[i - 1]
            i -= 1
        else:
            if nums1[i - 1] > nums2[j - 1]:
                nums1[k-1] = nums1[i-1]
                i -= 1
            else:
                nums1[k-1] = nums2[j-1]
                j -= 1
        k -= 1
    print(nums1)


def missingNumber(nums):
    """
    268. 缺失数字
    给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
    示例 1:
    输入: [3,0,1]
    输出: 2
    示例 2:
    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8
    说明:
    你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
    :param nums: List[int]
    :return: int
    """
    """
    # 桶排序 43%
    nums.append(-1)
    n = len(nums)
    for i in range(n):
        while nums[i] >= 0 and nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return nums.index(-1)
    """
    """
    # 求和
    cur = 0
    total = 0
    n = len(nums)
    for i in range(n):
        cur += nums[i]
        total += i
    return total + n - cur
    """
    # 异或 a^a^b^b^c=c
    n = len(nums)
    ans = n
    for i in range(n):
        ans ^= nums[i]
        ans ^= i
    return ans


def intersection(nums1, nums2):
    """
    349. 两个数组的交集
    给定两个数组，编写一个函数来计算它们的交集。
    示例 1:
    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2]
    示例 2:
    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [9,4]
    说明:
    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。
    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]
    """
    nums1 = sorted(list(set(nums1)))
    nums2 = sorted(list(set(nums2)))
    n1, n2 = len(nums1), len(nums2)
    i, j = 0, 0
    res = []
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
    return res


def isPerfectSquare(num):
    """
    给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
    说明：不要使用任何内置的库函数，如  sqrt。
    示例 1：
    输入：16
    输出：True
    示例 2：
    输入：14
    输出：False
    :param num: int
    :return: bool
    """
    """
    # 暴力
    i = 0
    while i ** 2 < num:
        i += 1
    return i ** 2 == num
    """
    """
    # 等差数列公式 1+3+5+...+(2n-1) = n^2
    ans, i = 0, 1
    while ans < num:
        ans += i
        i += 2
    return ans == num
    """
    # 牛顿迭代公式
    n = num
    while True:
        if (n - 1) ** 2 <= num and (n + 1) ** 2 >= num:
            break
        n = n - ((n ** 2) - num) // (2 * n)
    for i in range(3):
        if (n + i - 1) ** 2 == num:
            return True
    return False


def guessNumber(n):
    """
    374. 猜数字大小
    我们正在玩一个猜数字游戏。 游戏规则如下：
    我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
    每次你猜错了，我会告诉你这个数字是大了还是小了。
    你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
    -1 : 我的数字比较小
     1 : 我的数字比较大
     0 : 恭喜！你猜对了！
    示例 :
    输入: n = 10, pick = 6
    输出: 6
    :param n: int
    :return: int
    """
    pick = 1
    def guess(m):
        if m > pick: return -1
        elif m < pick: return 1
        else: return 0
    l, r, mid = 1, n, 0
    while l <= r:
        mid = l + (r - l)//2
        a = guess(mid)
        if a < 0:
            r = mid - 1
        elif a > 0:
            l = mid + 1
        else:
            break
    return mid


if __name__ == '__main__':
    print(guessNumber(1))
    # print(isPerfectSquare(16))
    # print(missingNumber([3, 0, 1]))
    # merge([2,0], 1, [1], 1)
    # print(gcdOfStrings("AAAAAAAA", "AAAAAAAA"))
    # findContentChildren([1,2], [1,2,3])
    # print(canPlaceFlowers([0], 1))
    # print(isPowerOfFour(16))
    # for i in range(10, 201):
    #     addDigits(i)
    # print(reverseVowels('leetcode'))
    pass
    # print(isUgly(14))
    # x = construct_tree_node([10,5,-3,3,2,None,11,3,-2,None,1])
    # ans = pathSum(x, 8)
    # print(ans)
    # findDisappearedNumbers([4,3,2,7,8,2,3,1])
    # findNthDigit(10)
    # x = construct_tree_node([1,2,3,None,5])
    # print(binaryTreePaths(x))
    # x = construct_list_node([1,2])
    # print(isPalindrome(x))
    # moveZeroes([0,1,0,3,13])
    # print(containsNearbyDuplicate([1,2,3,1,2,3], 2))