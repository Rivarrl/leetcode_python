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


def searchRange(nums, target):
    """
    34. 在排序数组中查找元素的第一个和最后一个位置
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    l = len(nums)
    if l == 0: return [-1, -1]
    i, j = 0, l - 1
    while i < j:
        m = (i + j) >> 1
        if nums[m] > target:
            j = m - 1
        elif nums[m] < target:
            i = m + 1
        else:
            i = j = m
    # print(i, j)
    if nums[i] != target and nums[j] != target:
        return [-1, -1]
    pi, pj = False, False
    while i >= 0 and nums[i] == target:
        i -= 1
        pi = True
    while j < l and nums[j] == target:
        j += 1
        pj = True
    i = i + 1 if pi else i
    j = j - 1 if pj else j
    # print(i, j)
    return [i, j]


if __name__ == '__main__':
    # print(jump([2, 3, 1, 1, 4]))
    searchRange([1,1,2], 1)
    pass
