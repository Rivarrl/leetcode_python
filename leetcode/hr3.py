from typing import List

from algorithm_utils import *

@timeit
def minimumMoves(arr: List[int]) -> int:
    """
    5115. 删除回文子数组
    给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
    注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
    请你计算并返回从数组中删除所有数字所需的最少操作次数。
    示例 1：
    输入：arr = [1,2]
    输出：2
    示例 2：
    输入：arr = [1,3,4,1,5]
    输出：3
    解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
    提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 20
    """
    n = len(arr)
    dp = [[n] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][i] = 1
        dp[i-1][i] = 1 if arr[i-1] == arr[i] else 2
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                for x in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][x] + dp[x+1][j])
    print(dp)
    return dp[0][n-1]


@timeit
def minimumMoves2(arr):
    def fdp(i, j):
        if i > j: return 0
        if i == j: return 1
        if i + 1 == j:
            if arr[i] == arr[j]:
                return 1
            else:
                return 2
        if dp[i][j] != -1:
            return dp[i][j]
        res = n
        for k in range(i, j+1):
            if arr[i] != arr[k]: continue
            left = fdp(i+1, k-1)
            if left == 0: left = 1
            res = min(res, left + fdp(k+1, j))
        dp[i][j] = res
        return res
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]
    res = fdp(0, n-1)
    print(dp)
    return res


def isGoodArray(nums: List[int]) -> bool:
    """
    5250. 检查「好数组」
    给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
    假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
    示例 1：
    输入：nums = [12,5,7,23]
    输出：true
    解释：挑选数字 5 和 7。
    5*3 + 7*(-2) = 1
    示例 2：
    输入：nums = [29,6,10]
    输出：true
    解释：挑选数字 29, 6 和 10。
    29*1 + 6*(-3) + 10*(-1) = 1
    示例 3：
    输入：nums = [3,6]
    输出：false
    提示：
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    """
    def gcd(x, y):
        if x == 0: return y
        return gcd(y%x, x)
    n = len(nums)
    if n == 1: return nums[0] == 1
    c = nums[0]
    for i in range(1, n):
        c = gcd(c, nums[i])
        if c == 1: return True
    return False


if __name__ == '__main__':
    res = isGoodArray([1])
    print(res)
    # res = minimumMoves([16,6,14,6,7,6,20,6,5,4,20,19,8,13,11,7,7,5,2,19,14,6,20,10,10,4,9,5,19,10,11,16,3,9,9,6,18,1,3,12,12,11,17,3,11,11,7,16,12,12,5,8,7,10,15,20,3,15,9,10,11,11,2,1,15,19,4,11,15,19,17,13,10,20,20,19,8,6,2,14,12,5,2,4,16,10,3,4,4,12,2,6,5,9,15,4,10,2,15,15])
    # print(res)
    # res = minimumMoves2([16,6,14,6,7,6,20,6,5,4,20,19,8,13,11,7,7,5,2,19,14,6,20,10,10,4,9,5,19,10,11,16,3,9,9,6,18,1,3,12,12,11,17,3,11,11,7,16,12,12,5,8,7,10,15,20,3,15,9,10,11,11,2,1,15,19,4,11,15,19,17,13,10,20,20,19,8,6,2,14,12,5,2,4,16,10,3,4,4,12,2,6,5,9,15,4,10,2,15,15])
    # print(res)
    pass
