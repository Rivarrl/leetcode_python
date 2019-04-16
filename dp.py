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


def lis_ex1(nums):
    """
    VIJOS1098
    选合唱队成员
    N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形
    合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1, 2, …, K，他们的身高分别为T1, T2, …, TK
    则他们的身高满足T1 < T2 < … < Ti , Ti > Ti+1 > … > TK (1 <= i <= K)
    你的任务是已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形
    例如: nums = [186, 186, 150, 200, 160, 130, 197, 220] res = 4 去掉186 186(或150) 197 220
    思路: 将每个同学作为中心，分别去求其左侧的最长递增序列和右侧的最长递减序列，总人数 - (两侧相加 - 1)即为所得
    :param nums: List[int]
    :return: int
    """
    total = nums.__len__()
    dph = [1 for _ in nums]
    dpt = [1 for _ in nums]
    for i in range(total):
        ri = total - 1 - i
        for j in range(i):
            rj = total - 1 - j
            if nums[i] > nums[j] and dph[i] <= dph[j]:
                dph[i] = dph[j] + 1
            if nums[ri] > nums[rj] and dpt[ri] <= dpt[rj]:
                dpt[ri] = dpt[rj] + 1
    res = 0
    for i in range(total):
        if dph[i] + dpt[i] > res:
            res = dph[i] + dpt[i]
    return total + 1 - res


def max_sub_rec(nums):
    """
    最大子段和
    给定n个整数组成的序列a1,a2,…,an，求该序列子段和的最大值。
    最大子段和不能是负数，当序列中均为负数时定义最大子段和为0。
    例如: [-2, 11, -4, 13, -5, -2]的最大子段([11, -4, 13])和为20。
    思路1(递归): 首先可以想到用分治的方法解决这个问题，如果将给定的序列a[1…n]分成长度相等的两段a[1…n//2]和a[n//2+1…n]，分别求出这两段的最大子段和。
        则该给定序列的最大子段和有三种情况：
            1. 和a[1…n//2]的最大子段和相同；
            2. 和a[n//2+1…n]的最大子段和相同；
            3. 最大子段和包含两部分。
        前两种情形我们可以用递归方法求出，第三种情形可以分别求出两部分的最大子段和值再相加。序列的最大子段和即为这三种情形的最大值。
    :param nums: List[int]
    :return: int
    """
    l = len(nums)

    def inner(sn, l, r):
        """
        内部函数，递归用
        :param sn: List[int]
        :param l: int
        :param r: int
        :return: int
        """
        if l == r:
            return sn[l]
        mid = (l + r) // 2
        s1 = inner(sn, l, mid)
        s2 = inner(sn, mid + 1, r)
        i, j = mid, mid + 1
        s31 = sn[i]
        s32 = sn[j]
        while (i > l and s31 + sn[i - 1] > s31):
            s31 += sn[i - 1]
            i -= 1
        while (j < r and s32 + sn[j + 1] > s32):
            s32 += sn[j + 1]
            j += 1
        s3 = s31 + s32
        return max(s1, s2, s3)

    return inner(nums, 0, l - 1)


def max_sub_dp(nums):
    """
    最大子段和
    给定n个整数组成的序列a1,a2,…,an，求该序列子段和的最大值。
    最大子段和不能是负数，当序列中均为负数时定义最大子段和为0。
    例如: [-2, 11, -4, 13, -5, -2]的最大子段([11, -4, 13])和为20。
    思路2(动态规划): 利用一维数组dp，dp[i]表示从0到i的子串最大和(max(nums[j:i]) for j in (0, i))
    :param nums: List[int]
    :return: int
    """
    l = len(nums)
    dp = [nums[0]]
    dp.extend([0] * (l - 1))
    for i in range(1, l):
        dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
    return max(dp)


def max_of_two_sub(nums):
    """
    POJ2593
    求数组里不相交的两个子串和的最大值
    例如：
    nums = [-5, 9, -5, 11, 20]
    res = 40
    思路：
    从左向右遍历求以nums[i]结尾的子串求和最大值存入dp，再从右向左遍历求以nums[i]为开头的子串求和最大值，再将改值加dp[i-1]取最大值即为所求
    nums = [-5, 9, -5, 11, 20]
    left =  [0, -5, 9, 9, 15, 35] 为防止越界left[0] = 0
    right = [40, 40, 31, 31, 20]
    max(right[i] + left[i-1]) = 31 + 9 = 40
    :param nums: List[int]
    :return: int
    """
    inf = 2**31
    l = nums.__len__()
    dp = [0]
    dp.extend([-inf for _ in range(l)])
    sum, m = 0, -inf
    for i in range(l):
        sum += nums[i]
        if sum > m:
            m = sum
        dp[i + 1] = m
        if sum < 0:
            sum = 0
    sum, m = 0, -inf
    ans = m
    for i in range(l):
        j = l - 1 - i
        sum += nums[j]
        if sum > m:
            m = sum
        t = m + dp[j]
        if t > ans:
            ans = t
        if sum < 0:
            sum = 0
    return ans


def max_sub_matrix(matrix):
    """
    POJ1050
    求矩阵中的最大的子矩阵和
    例如：
    matrix = [[0, -2, 7, 0],
              [9, 2, -6, 2],
              [-4, 1, -4, 1],
              [-1, 8, 0 ,-2]]
    res = 15
    因为子矩阵[[9, 2], [-4, 1], [-1, 8]]值最大
    思路：
    将第i行至第j行合并，matrix[i][k] + matrix[j][k]逐项相加，降成一维数组求最长子串长度，最大值即为所求
    :param matrix: List[int]
    :return: int
    """
    def inner_maxsub(nums):
        m = -inf
        tmp = -1
        for i in range(col):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            if tmp > m:
                m = tmp
        return m

    inf = 2**31
    inner_sum = lambda n1, n2: [x + y for x, y in zip(n1, n2)]
    row = matrix.__len__()
    col = matrix[0].__len__()

    m = -inf
    for i in range(row):
        fit_row = [0 for _ in range(col)]
        for j in range(i, row):
            fit_row = inner_sum(fit_row, matrix[j])
            tmp = inner_maxsub(fit_row)
            if tmp > m:
                m = tmp
    return m


def convex_polygon(weight):
    """
    用多边形顶点的逆时针序列表示凸多边形，即P={V0,V1,…,Vn}表示具有n+1条边的凸多边形。
    给定凸多边形P，以及定义在由多边形的边和弦组成的三角形上的权函数w。
    要求确定该凸多边形的三角剖分，使得即该三角剖分中诸三角形上权之和为最小。
    思路：
    若P={V0,V1……Vn}的最优三角剖分T包含三角形V0VkVn,则T的权为三个部分权之和：三角形V0VkVn的权，多边形{V0,V1……Vk}的权和多边形{Vk,Vk+1……Vn}的权之和。
    可以断言，由T确定的这两个子多边形的三角剖分也是最优的。
    设t[i][j]为凸多边形{Vi-1,Vi……Vj}的最优三角剖分所对应的最优权值，则P的最优权值为t[1][n]，有：
    t[i][j] = 0 if i==j else min(t[i][k] + t[k+1][j] + w(vi-1, vk, vj)) w(x,y,z)表示三角形xyz的权值和
    :param weight: List[List[int]]
    :return: int
    """

    def inner(i, j, s):
        if i == j:
            return
        inner(i, s[i][j], s)
        inner(s[i][j] + 1, j, s)
        print("三角剖分顶点：V%d, V%d, V%d"% (i-1, j, s[i][j]))

    inf = 2 ** 31
    l = weight.__len__()
    t, s = [[0 for _ in range(l + 1)] for _ in range(l + 1)], [[0 for _ in range(l + 1)] for _ in range(l + 1)]
    for r in range(2, l + 1):
        for i in range(1, l + 1 - r):
            j = i + r - 1
            m = inf
            for k in (i, j):
                t[i][j] = t[i][k] + t[k+1][j] + (weight[i-1][k] + weight[k][j] + weight[j][i-1])
                if t[i][j] < m:
                    m = t[i][j]
                    s[i][j] = k
            t[i][j] = m
    print(s)
    print(t)
    print(l)
    print("此多边形的最优三角剖分值为：", t[1][l-1])
    print("最优三角剖分结构为：")
    inner(1, l - 1, s)

if __name__ == '__main__':
    # q1in1 = [1, 3, 2, 4, 2]
    # res1 = min_of_multiply(q1in1)
    # print(res1)

    # q2in1 = [[7, 0, 0, 0, 0], [3, 8, 0, 0, 0], [8, 1, 0, 0, 0], [2, 7, 4, 4, 0], [4, 5, 2, 6, 5]]
    # q2in2 = 2
    # res2 = triangle_max_pace(q2in1, q2in2)
    # print(res2)

    # q3in1 = "ABCBDAB"
    # q3in2 = "BDCABA"
    # res3 = lcs(q3in1, q3in2)
    # print(res3)

    # q3_2in1 = "Ab3bd"
    # res3_2 = palindrome(q4in1)
    # print(res3_2)

    # q4in1 = [0, 3, 1, 2, 5, 9, 4, 14, 10, 12]
    # res4 = lis(q4in1)
    # print(res4)
    # res4_2 = lis_2(q4in1)
    # print(res4_2)

    # q4ex1in1 = [186, 186, 150, 200, 160, 130, 197, 220]
    # res4_ex1 = lis_ex1(q4ex1in1)
    # print(res4_ex1)

    # q5in1 = [-2, 11, -4, 13, -5, -2]
    # res5 = max_sub_rec(q5in1)
    # print(res5)
    # res5_2 = max_sub_dp(q5in1)
    # print(res5_2)

    # q6in1 = [-5, 9, -5, 11, 20]
    # res6 = max_of_two_sub(q6in1)
    # print(res6)

    # q7in1 = [[0, -2, -7, 0],
    #          [9, 2, -6, 2],
    #          [-4, 1, -4, 1],
    #          [-1, 8, 0 ,-2]]
    # res7 = max_sub_matrix(q7in1)
    # print(res7)

    q8in1 = [[0,2,2,3,1,4],[2,0,1,5,2,3],[2,1,0,2,1,4],[3,5,2,0,6,2],[1,2,1,6,0,1],[4,3,4,2,1,0]]
    res8 = convex_polygon(q8in1)