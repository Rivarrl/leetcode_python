# -*- coding: utf-8 -*-
# ======================================
# @File    : 401.py
# @Time    : 2019/11/15 15:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [401. 二进制手表](https://leetcode-cn.com/problems/binary-watch/)
    """
    @timeit
    def readBinaryWatch(self, num: int) -> List[str]:
        """
        思路：回溯算法，dfs状态转移有当前位置灯亮和不亮两种选择。
        为灯的亮灭设置一个数组，由于只有亮灭两种状态，可以压缩成二进制表示（二进制题当然要充分使用二进制操作了）
        """
        def count1(x):
            # x二进制数1
            ctr = 0
            while x:
                x &= (x - 1)
                ctr += 1
            return ctr

        def get_mask():
            h_mask = 0
            for i in range(9, 5, -1):
                h_mask |= (1 << i)
            m_mask = h_mask ^ ((1 << 10) - 1)
            return h_mask, m_mask

        def ttt(x):
            # transfer to time，二进制转成时间
            h_mask, m_mask = get_mask()
            th, tm = (x & h_mask) >> 6, (x & m_mask)
            return "%s:%s" % (str(th), str(tm).zfill(2))

        def vt(x):
            # valid time，判断是不是时间，如8+4+2=14小时，超过题目要求的0-11: return false
            h_mask, m_mask = get_mask()
            if (x & h_mask) >> 6 > 11: return False
            if (x & m_mask) > 59: return False
            return True

        # 分6位时4位，从低到高先分后时
        x = 0
        def dfs(i, x):
            # 时间越界部分，剪枝
            if not vt(x): return
            ctr = count1(x)
            # 乐观估计剪枝，10-i:当前还可以再加几个1，ctr:当前有几个1
            if 10 - i + ctr < num : return
            # 终止条件
            if i == 10:
                ctr == num and res.append(ttt(x))
                return
            dfs(i + 1, x | (1 << i))
            dfs(i + 1, x)
        res = []
        dfs(0, x)
        return res


if __name__ == '__main__':
    a = Solution()
    a.readBinaryWatch(1)