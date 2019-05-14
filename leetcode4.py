from algorithm_utils import *

# leetcode 4

def jump(nums):
    """
    45. 跳跃游戏 II
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    说明:
    假设你总是可以到达数组的最后一个位置。
    :param nums: List[int]
    :return: int
    """
    """
    # 超时
    l = len(nums)
    if l < 2: return 0
    dp = [l for _ in range(l)]
    dp[0] = 0
    dp[1] = 1
    for i in range(l):
        for j in range(i):
            if i - j <= nums[j]:
                dp[i] = min(dp[i], dp[j] + 1)
    # print(dp)
    return dp[-1]
    """
    l = len(nums)
    if l < 2: return 0
    ans, i, r, n = 0, 0, 0, nums[0]
    for i in range(l):
        n = max(i + nums[i], n)
        if n >= l - 1: return ans + 1
        if i == r:
            ans += 1
            r = n
    return ans


if __name__ == '__main__':
    print(jump([2, 3, 1, 1, 4]))
    pass
