# -*- coding: utf-8 -*-
# ======================================
# @File    : 564.py
# @Time    : 2019/12/9 18:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [564. 寻找最近的回文数](https://leetcode-cn.com/problems/find-the-closest-palindrome/)
    """
    @timeit
    def nearestPalindromic(self, n: str) -> str:
        """
        思路:
        把n的长度设为length.
        根据n的长相, 分为是回文串和不是回文串两种情况:
            是回文串的话:
                需要考虑两种情况:
                    case1: 形如x000x 或 x9999x, 例如19991 ~ 20002
                    case1可以根据首尾数字大小直接写出最终返回的结果
                    case2: 18181 ~ 18281 / 18081; 1221 ~ 1331 / 1111
                    case2对每一位添加/删除的字符串合起来看也是回文结构的, 那么最小代价一定是00100或者0110这样的
                    注意上面举例的数+或-结果相同的时候都选择较小的
                    由于case1和case2的判断用的是夹在中间的部分是否全为0或9,
                    对于特殊情况(length == 2时all函数会直接通过的)特殊处理: 分为11和99和其他, 单独写个分支
            不是回文串的话:
                特殊情况(就是上面的case1):
                    如果是x9999y或者x0000y, 那最近的回文数走几步就能找到, 枚举查找一下即可.
                一般情况:
                    length为奇数时:
                        对中位数的两侧的值, 计算它们的距离
                        距离<=5时不需要改变中位数的值
                        1, 6 -> 1, 1; 6, 1 -> 6, 6
                        距离>5时,中位数需要+/-1
                        如0x8 -> 0(x+1)0; 8x0 -> 8(x-1)8
                        * 这里注意如果产生进位/借位需要相应修改高位的值
                          我一开始没注意这点竟然也过了, 提供个测试用例"1170131", 我没考虑进位的代码直接输出的是"117-711"
                    length为偶数时:
                        整两个分支, 分别计算+和-的情况
                        中间的两个值xy对应+和-只能变成xx或(x-1x-1和x+1x+1二选一)
                        二选一是因为当x<y的时候不可能是x-1x-1, 因为减的途中已经经过xx, x>y时同理
                        注意如果两个分支计算的距离相等的时候取较小的一个..
                        否则取距离较小的一个
        """
        length = len(n)
        if length == 1: return str((int(n) - 1 + 10) % 10)
        mid = length // 2
        if n == n[::-1]:
            if length == 2:
                if n == '11': return '9'
                elif n == '99': return '101'
                else: return str(int(n) - 11)
            # case1
            if all(e == '9' for e in n[1:-1]):
                x = int(n[0]) + 1
                if x == 10: return '10' + '0' * (length - 2) + '1'
                return str(x) + '0' * (length - 2) + str(x)
            elif all(e == '0' for e in n[1:-1]):
                x = int(n[0]) - 1
                if x == 0: return '9' * (length - 1)
                return str(x) + '9' * (length - 2) + str(x)
            else:
                # case2
                if length & 1:
                    if int(n[mid]) > 0:
                        return n[:mid] + str(int(n[mid]) - 1) + n[mid+1:]
                    else:
                        return n[:mid] + str(int(n[mid]) + 1) + n[mid+1:]
        else:
            # case1
            if all(e == '0' or e == '9' for e in n[1:-1]):
                nums = [int(n), int(n)]
                while 1:
                    nums[0] -= 1
                    nums[1] += 1
                    if str(nums[0]) == str(nums[0])[::-1]: return str(nums[0])
                    if str(nums[1]) == str(nums[1])[::-1]: return str(nums[1])
            else:
                ret = [int(e) for e in n]
                if length & 1:
                    i, j = mid - 1, mid + 1
                else:
                    i, j = mid - 1, mid
                dis = abs(ret[i] - ret[j])
                if length & 1:
                    if dis <= 5:
                        ret[j] = ret[i]
                    else:
                        if ret[j] > ret[i]:
                            ret[mid] += 1
                            if ret[mid] == 10:
                                ret[mid] = 0
                                ret[i] += 1
                        else:
                            ret[mid] -= 1
                            if ret[mid] == -1:
                                ret[mid] = 9
                                ret[i] -= 1
                        ret[j] = ret[i]
                    for k in range(1, mid):
                        x, y = i - k, j + k
                        if ret[x] != ret[y]: ret[y] = ret[x]
                else:
                    from functools import reduce
                    ret2 = ret[:]
                    if ret[j] > ret[i]:
                        ret[i] += 1
                    else:
                        ret[i] = (ret[i] - 1 + 10) % 10
                    ret[j], ret2[j] = ret[i], ret2[i]
                    for k in range(1, mid):
                        x, y = i - k, j + k
                        if ret[x] != ret[y]: ret[y] = ret[x]
                        if ret2[x] != ret2[y]: ret2[y] = ret2[x]
                    f = lambda x, y: x * 10 + y
                    r1, r2 = reduce(f, ret), reduce(f, ret2)
                    if abs(r1 - int(n)) == abs(r2 - int(n)):
                        ret = ret2 if r2 < r1 else ret
                    else:
                        ret = [ret, ret2][abs(r1 - int(n)) > abs(r2 - int(n))]
                return ''.join([str(e) for e in ret])


if __name__ == '__main__':
    a = Solution()
    # a.nearestPalindromic("123")
    # a.nearestPalindromic("12932")
    # a.nearestPalindromic("99800")
    # a.nearestPalindromic("12120")
    # a.nearestPalindromic("20001")
    # a.nearestPalindromic("8942")
    # a.nearestPalindromic("8943")
    # a.nearestPalindromic("8944")
    # a.nearestPalindromic("11")
    # a.nearestPalindromic("1234")
    # a.nearestPalindromic("1213")
    # a.nearestPalindromic("1805170081")
    # ???
    a.nearestPalindromic("1170131")
    a.nearestPalindromic("1119731")