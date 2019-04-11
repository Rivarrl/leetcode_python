# -*- coding:utf-8 -*-
import algorithm_utils as alg


## 动态规划
## 核心思想，将问题化为子问题的解的和

def min_of_multiply(series):
    """
    POJ1651
    给定N个数，每次从中抽出一个数(第一和最后一个不能抽)，该次的得分即为抽出的数与相邻两个数的乘积。
    一直这样将每次的得分累加直到只剩下首尾两个数为止，问最小得分。
    思路：i到j长度的最小值= (i-k长度最小值) + (k-j长度最小值) + (最后一次得分(x[i] * x[j] * x[k]))
    :param series: List[int] 数组
    :return: int 最小得分
    """
    l = series.__len__()
    if l < 3:
        return -1
    if l == 3:
        return series[0] * series[1] * series[2]
    dp = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l - 2):
        dp[i][i + 2] = series[i] * series[i + 1] * series[i + 2]

    for w in range(3, l):
        for i in range(l - w):
            j = i + w
            for k in range(i + 1, j):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i][k] + dp[k][j] + series[i] * series[k] * series[j]
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + series[i] * series[k] * series[j])
    return dp[0][l - 1]


def triangle_max_pace(triangle):
    """
    POJ1163
    给定一个由n行数字组成的数字三角型，如图所示。
    设计一个算法，计算从三角形的顶至底的一条路径，使该路径经过的数字总和最大。路径上的每一步都只能往左下或右下走，给出这个最大和。
        7
       3 8
      8 1 0
     2 7 4 4
    4 5 2 6 5
    思路1 dp[i][j]来表示(i,j)点到终点的最大值
    :param triangle: List[List[int]]
    :return: int
    """
    l = triangle.__len__()
    dp = [[triangle[j][i] if j == l - 1 else 0 for i in range(l)] for j in range(l)]

    for i in range(l - 1):
        ri = l - i - 2
        for j in range(ri + 1):
            dp[ri][j] = max(dp[ri + 1][j], dp[ri + 1][j + 1]) + triangle[ri][j]
    return dp[0][0]


def triangle_max_pace_2(triangle):
    """
    POJ1163
    思路2：dp[i][j]来表示(0,0)点到(i,j)点的最大值
    :param triangle: List[List[int]]
    :return: int
    """
    l = triangle.__len__()
    dp = [[0 for _ in range(l)] for _ in range(l)]
    dp[0][0] = triangle[0][0]
    for i in range(1, l):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][-1] = triangle[i][-1] + dp[i - 1][-1]
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return max(dp[-1])


def lcs(s1, s2):
    """
    POJ1458
    查询最长公共子序列的长度
    例如：X = 'ABCBDAB' Y = 'BDCABA' sub='BCBA' max_sub_len = 4
    思路：使用二维数组dp，dp[i][j]表示X[0:i] 和 Y[0:j]子串的最长公共子序列长度
    :param s1: str
    :param s2: str
    :return: int
    """
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i > 0 and j > 0:
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def palindrome(s):
    """
    组成回文词需要插入最少的字符数，lcs的应用
    例如: s = "Ab3bd" res = 2  ∵ Ab3bd -> Adb3bdA/dAb3bAd
    思路: 将s反转和s取最长公共子序列长度，用s长度减去子序列长度即为答案
    :param s: str
    :return: int
    """
    return len(s) - lcs(s, s[::-1])


def lis(list_num):
    """
    POJ2533
    最长递增子序列
    例如: list_num = [0, 3, 1, 2, 4] res = 4 ∵ 0124
    思路: 与lcs类似，使用一维数组dp，dp[i]表示list_num[0:i]的最长递增子序列
    复杂度: O(n^2)
    :param list_num: List[int]
    :return: int
    """
    l = list_num.__len__()
    dp = [1 for _ in range(l)]
    for i in range(1, l):
        for j in range(i):
            if list_num[j] < list_num[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_2(list_num):
    """
    POJ2533
    思路2: 空数组添加的方法，如果当前值大于队尾，就插入到队尾，否则使用二分查找找到第一个比他大的数替换掉，最后数组长度即为结果
          dp[i]表示所有长度为i+1的子串的末尾值中的最小值
    复杂度: O(nlogn)
    :param list_num: List[int]
    :return: int
    """
    l = len(list_num)
    dp = [list_num[0]]
    for i in range(1, l):
        if list_num[i] > dp[-1]:
            dp.append(list_num[i])
        else:
            dp[alg.binary_search(dp, 0, dp.__len__() - 1, list_num[i])] = list_num[i]
    return dp.__len__()


if __name__ == '__main__':
    # res1 = min_of_multiply([1, 3, 2, 4, 2])
    # print(res1)

    # tri = [[7, 0, 0, 0, 0], [3, 8, 0, 0, 0], [8, 1, 0, 0, 0], [2, 7, 4, 4, 0], [4, 5, 2, 6, 5]]
    # res2 = triangle_max_pace(tri, 2)
    # print(res2)

    # s1 = "ABCBDAB"
    # s2 = "BDCABA"
    # res3 = lcs(s1, s2)
    # print(res3)

    # s = "Ab3bd"
    # res3_ex1 = palindrome(s)
    # print(res3_ex1)

    q = [0, 3, 1, 2, 5, 9, 4, 14, 10, 12]
    res4 = lis(q)
    print(res4)
    res4_2 = lis_2(q)
    print(res4_2)