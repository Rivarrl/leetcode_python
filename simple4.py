# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 简单题 4

def numberOfBoomerangs(points):
    """
    447. 回旋镖的数量
    给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
    找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
    示例:
    输入:
    [[0,0],[1,0],[2,0]]
    输出:
    2
    解释:
    两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
    :param points: List[List[int]]
    :return: int
    """
    """
    # 终极暴力，超时
    n = len(points)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            x1 = abs(points[i][0] - points[j][0])
            y1 = abs(points[i][1] - points[j][1])
            z1 = x1 ** 2 + y1 ** 2
            for k in range(n):
                if i == k or j == k: continue
                x2 = abs(points[i][0] - points[k][0])
                y2 = abs(points[i][1] - points[k][1])
                z2 = x2**2 + y2**2
                if z1 == z2: ans += 1
    print(ans)
    return ans
    """
    # 优化：以每个点作为中心点记录与其他点的距离，存入哈希表中，C(2,n)中每两步之间相差2n， n*(n+1) = (n-1)*n + 2n
    n = len(points)
    ans = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                z = x**2 + y**2
                if not z in d:
                    d[z] = 1
                else:
                    ans += d[z] * 2
                    d[z] += 1
        d = {}
    return ans


def canConstruct(ransomNote, magazine):
    """
    383. 赎金信
    给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
    (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
    注意：
    你可以假设两个字符串均只含有小写字母。
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    :param ransomNote: str
    :param magazine: str
    :return: bool
    """
    d = [0] * 26
    for x in magazine:
        d[ord(x) - ord('a')] += 1
    for x in ransomNote:
        if d[ord(x) - ord('a')] == 0:
            return False
        d[ord(x) - ord('a')] -= 1
    return True


def longestPalindrome(s):
    """
    409. 最长回文串
    给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
    在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
    注意:
    假设字符串的长度不会超过 1010。
    示例 1:
    输入:
    "abccccdd"
    输出:
    7
    解释:
    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
    :param s: str
    :return: int
    """
    """
    # 计数, A在前, a在后  30%
    d = [0] * 52
    a, z, A, Z = ord('a'), ord('z'), ord('A'), ord('Z')
    for x in s:
        if A <= ord(x) <= Z:
            d[ord(x)-A] += 1
        else:
            d[26 + ord(x)-a] += 1
    ans = 0
    flag = False
    for x in d:
        if x % 2 == 1:
            ans += x - 1
            flag = True
        else:
            ans += x
    ans += (not not flag)
    print(d)
    print(ans)
    return ans
    """
    # 使用set, x出现过就执行ans+2, 删掉x  30%
    d = set()
    ans = 0
    for x in s:
        if x in d:
            ans += 2
            d.remove(x)
        else:
            d.add(x)
    ans += (not not d)
    print(ans)
    return ans


if __name__ == '__main__':
    a = "aabbccd"
    longestPalindrome(a)
    # numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
    pass