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


if __name__ == '__main__':
    m = min_of_multiply([1, 3, 2, 4, 2])
    print(m)
