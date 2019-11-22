# -*- coding: utf-8 -*-
# ======================================
# @File    : 866.py
# @Time    : 2019/11/23 0:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [866. 回文素数](https://leetcode-cn.com/problems/prime-palindrome/)
    """
    def primePalindrome(self, N: int) -> int:
        """
        思路：暴力解吧，由于判断素数的复杂度高，题说了一定存在解。就从N开始加，先判断是不是回文数，再判断是不是素数
        """
        def r(x): return str(x) == str(x)[::-1]
        def p(x): return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
        while N > 0:
            if r(N) and p(N): return N
            N += 1


    def primePalindrome2(self, N: int) -> int:
        """
        高排名代码，优化两个操作。
        """
        def judge_pri(n):
            if (n+1)%6!=0 and (n-1)%6!=0:
                return False
            left,right = 2,n//2
            while left <=right:
                if n%left == 0:
                    return False
                else:
                    left += 1
                    right = n//left
            return True
        def find_pal(num):
            res = str(num)
            n = len(res)//2
            if res[n-1::-1] >= res[n+1:]:
                return int(res[:n+1]+res[n-1::-1])
            else:
                if res[n]!='9':
                    t = str(int(res[n])+1)
                    return int(res[:n]+t+res[n-1::-1])
                else:
                    a = str(int(res[:n])+1)
                    if len(a)>n:
                        return 10*(2*n+1)+1
                    else:
                        return int(a+'0'+a[::-1])
        if N == 1:
            return 2
        elif N < 4:
            return N
        elif N<6:
            return 5
        elif N<8:
            return 7
        elif N<12:
            return 11
        K = len(str(N))
        if K%2==0:
            return self.primePalindrome(10**K+1)
        else:
            res = find_pal(N)
            if judge_pri(res):
                return res
            else:
                return self.primePalindrome(res+1)


if __name__ == '__main__':
    a = Solution()
    a.primePalindrome(6)