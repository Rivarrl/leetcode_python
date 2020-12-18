# -*- coding: utf-8 -*-
# ======================================
# @File    : 636.py
# @Time    : 2020/12/18 12:19 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [636. 函数的独占时间](https://leetcode-cn.com/problems/exclusive-time-of-functions/)
    """
    @timeit
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        arr = [log.split(':') for log in logs]
        arr = [[int(e[0]), e[1], int(e[2])] for e in arr]
        arr.sort(key=lambda x:x[2])
        stk = []
        res = [0] * n
        for i in range(len(arr)):
            cur = arr[i]
            if cur[1] == 'start':
                stk.append([cur[0], cur[2], 0])
            else:
                last = stk.pop()
                x = cur[2] - last[1] + 1
                res[last[0]] += x - last[2]
                if stk:
                    stk[-1][-1] += x
        return res


if __name__ == '__main__':
    a = Solution()
    a.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
    a.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])
    a.exclusiveTime(8, ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"])