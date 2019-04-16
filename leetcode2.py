# -*-coding:utf-8-*-
# leetcode.py 内容太杂了，新起一个leetcode2.py

# 数数字，1->11->21->1211->.....
# 1 -> 11(1个1)
# 11 -> 21(2个1)
def counting_nums(t):
    def inner(num):
        l = num.__len__()
        res = ""
        i = 0
        while i < l:
            j = i
            count = 0
            while num[j] == num[i]:
                j += 1
                count += 1
                if j == l:
                    break
            res += str(count) + num[i]
            i = j
        return res

    result = "1"
    for _ in range(t - 1):
        result = inner(result)
    return result


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = nums.__len__()
    if l <= 1:
        return l
    i = 0
    while i < l - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i + 1])
            l -= 1
        else:
            i += 1
    return l


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    ls = str.strip('"').lstrip()
    i, k = 0, 0
    if ls.__len__() == 0 or (ls.__len__() == 1 and ls[0] == '-'):
        return 0
    try:
        _ = int(ls[0])
    except:
        if ls[0] == '-':
            i, k = 1, 1
        elif ls[0] == '+':
            i, k = 1, 2
        else:
            return 0
    while i < ls.__len__():
        if isint(ls[i]):
            i += 1
        else:
            # i -= 1
            break
    if i == 0:
        if k == 1 or k == 2:
            return 0
        else:
            return int(ls[0])
    res = ls[1:i] if k == 2 else ls[:i]
    if isint(res):
        if int(res) < int_min:
            return int_min
        elif int(res) > int_max:
            return int_max
        else:
            if res.rstrip('0') == '-':
                return 0
            return int(res)
    return 0


def isint(i):
    try:
        _ = int(i)
        return True
    except:
        return False

def countBits(num):
    """
    LC338
    比特位计数
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
    输入: 5
    输出: [0,1,1,2,1,2]
    进阶:
    给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
    要求算法的空间复杂度为O(n)。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数
    思路:
    动态规划，选用的思路1
    1) ans[i] = ans[i >> 1] + (i & 1)   # 取右移后的数一定比当前值小
    2) ans[i] = ans[i & (i - 1)] + 1    # i & (i - 1) < i
    3) ans[i*2] = ans[i]                # 注意越界问题
       ans[i*2+1] = ans[i] + 1
    :param num: int
    :return: List[int]
    """
    ans = [0 for _ in range(num + 1)]
    for i in range(1, num + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


def minPathSum(grid):
    """
    LC64
    最小路径和
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    输入: [[1,3,1],
          [1,5,1],
          [4,2,1]]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
    :param grid: List[List[int]]
    :return: int
    """
    row = grid.__len__()
    if row == 0:
        return 0
    col = grid[0].__len__()
    dp = [[0 for _ in range(col)] for _ in range(row)]
    r_sum, c_sum = 0, 0
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                if i == 0:
                    r_sum += grid[i][j]
                    dp[i][j] = r_sum
                if j == 0:
                    c_sum += grid[i][j]
                    dp[i][j] = c_sum
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

if __name__ == "__main__":
    # a = [[1,3,1],[1,5,1],[4,2,1]]
    # r = minPathSum(a)
    # print(r)
    # r = countBits(5)
    # print(r)
    print(1 << 31)