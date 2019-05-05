# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode3.py
# @Time    : 2019/4/27 0:47
# @Author  : Rivarrl
# ======================================

# leetcode3
from algorithm_utils import *


def divide(dividend, divisor):
    """
    29. 两数相除
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    说明:
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [-2**31,  2**31-1]。本题中，如果除法结果溢出，则返回 2**31-1。
    思路:
    用减法会超时，所以使用更快的位运算，<<1 = *2^1, >>1 = /2^1
    :param dividend: int
    :param divisor: int
    :return: int
    """
    inf = 2**31 - 1
    MAX = inf
    MIN = -inf - 1
    if dividend == 0 : return 0
    if divisor == 1: return dividend
    if dividend == MIN and divisor == -1: return MAX
    # 结果符号，两数（符号位）亦或
    f = dividend ^ divisor >= 0
    i, j = 0, 31
    a, b = abs(dividend), abs(divisor)
    res = 0
    while i < j:
        mid = (i + j) >> 1
        x = b << mid
        y = x << 1
        if y > a >= x:
            a -= x
            res += (1 << mid)
            i, j = 0, mid
        elif a < y:
            j = mid
        else:
            i = mid
    return res if f else -res


def maxCoins(nums):
    """
    312. 戳气球
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。
    说明:
    你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    示例:
    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
    :param nums: List[int]
    :return: int
    """
    pass


def combinationSum(candidates, target):
    """
    39. 组合总和
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。
    说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。
    示例 1:
    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
      [7],
      [2,2,3]
    ]
    示例 2:
    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """
    pass


def pancakeSort(A):
    """
    969. 煎饼排序
    给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
    返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
    示例 1：
    输入：[3,2,4,1]
    输出：[4,2,4,3]
    解释：
    我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
    初始状态 A = [3, 2, 4, 1]
    第一次翻转后 (k=4): A = [1, 4, 2, 3]
    第二次翻转后 (k=2): A = [4, 1, 2, 3]
    第三次翻转后 (k=4): A = [3, 2, 1, 4]
    第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
    :param A: List[int]
    :return: List[int]
    """
    pass




def threeSumClosest(nums, target):
    """
    16. 最接近的三数之和
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
    :param nums: List[int]
    :param target: int
    :return: int
    """
    l = len(nums)
    nums.sort()
    two_sum = [target - x for x in nums]
    resx = 2**31 - 1
    # print(nums)
    # print(two_sum)
    for k in range(l):
        i, j = 0, l - 1
        while i < j:
            if i == k:
                i += 1
                continue
            if j == k:
                j -= 1
                continue
            x = two_sum[k] - nums[i] - nums[j]
            # print(i, j, k, x)
            if x == 0:
                return target
            elif x > 0:
                i += 1
            else:
                j -= 1
            if abs(x) < abs(resx):
                resx = x
    # print(resx)
    return target - resx


def findBottomLeftValue(root):
    """
    513. 找树左下角的值
    给定一个二叉树，在树的最后一行找到最左边的值。
    示例 1:
    输入:
        2
       / \
      1   3
    输出:
    1
    示例 2:
    输入:
            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7
    输出:
    7
    注意: 您可以假设树（即给定的根节点）不为 NULL。
    :param root: TreeNode
    :return: int
    """
    def inner(r, c):
        c += 1
        if r.left and r.right:
            il = inner(r.left, c)
            ir = inner(r.right, c)
            if il[1] < ir[1]:
                return ir
            else:
                return il
        elif r.left:
            return inner(r.left, c)
        elif r.right:
            return inner(r.right, c)
        else:
            return [r, c]
    return inner(root, 0)[0].val


def minimumDeleteSum(s1, s2):
    """
    712. 两个字符串的最小ASCII删除和
    给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
    示例 1:
    输入: s1 = "sea", s2 = "eat"
    输出: 231
    解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
    在 "eat" 中删除 "t" 并将 116 加入总和。
    结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
    示例 2:
    输入: s1 = "delete", s2 = "leet"
    输出: 403
    解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
    将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
    结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
    如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
    注意:
    0 < s1.length, s2.length <= 1000。
    所有字符串中的字符ASCII值在[97, 122]之间。
    :param s1: str
    :param s2: str
    :return: int
    """
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 0:
        return sum(ord(x) for x in s2)
    if l2 == 0:
        return sum(ord(x) for x in s1)
    dp = [['' for _ in range(l1)] for _ in range(l2)]
    dp[0][0] = s1[0] + s2[0] if s1[0] != s2[0] else ''
    x, y = s1[0], s2[0]
    if x == y:
        dp[0][0] = ''
        x = ''
        y = ''
    else:
        dp[0][0] = x + y
    for i in range(1, l2):
        if s2[i] == x:
            dp[0][i] = dp[0][i-1].replace(x, '')
            x = ''
        else:
            dp[0][i] = dp[0][i-1] + s2[i]
    for i in range(1, l1):
        if s1[i] == y:
            dp[i][0] = dp[i-1][0].replace(y, '')
            y = ''
        else:
            dp[i][0] = dp[i-1][0] + s1[i]
    print(dp)
    for i in range(1, l2):
        for j in range(1, l1):
            if s1[j] == s2[i]:
                dp[i][j] = dp[i-1][j-1]
            else:
                t1 = dp[i][j - 1] + s2[i]
                t2 = dp[i-1][j] + s1[j]
                x1 = sum(ord(x) for x in t1)
                x2 = sum(ord(x) for x in t2)
                dp[i][j] = t1 if x1 < x2 else t2
    print(dp)
    return sum(ord(x) for x in dp[l2-1][l1-1])



if __name__ == '__main__':
    pass
    print(minimumDeleteSum("delete", "leet"))
    # print(divide(10,2))
    # print(threeSumClosest([1,6,9,14,16,70], 81))
    # x = TreeNode(5)
    # x.left = TreeNode(7)
    # y = TreeNode(3)
    # y.left = x
    # y.right = TreeNode(6)
    # z = TreeNode(2)
    # z.left = TreeNode(4)
    # t = TreeNode(1)
    # t.left = z
    # t.right = y
    # print(findBottomLeftValue(t))