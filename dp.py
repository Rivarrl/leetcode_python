# -*- coding:utf-8 -*-

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


def triangle_max_pace(triangle, method=1):
    """
    POJ1163
    给定一个由n行数字组成的数字三角型，如图所示。
    设计一个算法，计算从三角形的顶至底的一条路径，使该路径经过的数字总和最大。路径上的每一步都只能往左下或右下走，给出这个最大和。
        7
       3 8
      8 1 0
     2 7 4 4
    4 5 2 6 5
    思路：1) dp[i][j]来表示(i,j)点到终点的最大值
         2) dp[i][j]来表示(0,0)点到(i,j)点的最大值
    :param triangle: List[List[int]]
    :return: int
    """
    l = triangle.__len__()
    if (method == 1):
        # 思路1
        dp = [[triangle[j][i] if j == l - 1 else 0 for i in range(l)] for j in range(l)]

        for i in range(l - 1):
            ri = l - i - 2
            for j in range(ri + 1):
                dp[ri][j] = max(dp[ri + 1][j], dp[ri + 1][j + 1]) + triangle[ri][j]
        return dp[0][0]
    else:
        # 思路2
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
    :param s1: str
    :param s2: str
    :return: int
    """
    pass

if __name__ == '__main__':
    # m = min_of_multiply([1, 3, 2, 4, 2])
    # print(m)

    tri = [[7, 0, 0, 0, 0], [3, 8, 0, 0, 0], [8, 1, 0, 0, 0], [2, 7, 4, 4, 0], [4, 5, 2, 6, 5]]
    n = triangle_max_pace(tri, 2)
    print(n)
