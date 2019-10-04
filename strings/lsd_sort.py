# -*- coding: utf-8 -*-
# ======================================
# @File    : lsd_sort.py
# @Time    : 2019/10/4 15:21
# @Author  : Rivarrl
# ======================================
from strings.utils import *

class LSDSort:
    """
    低位优先字符串排序
    适用于等长字符串排序
    """
    def sort(self, arr, W):
        """
        排序
        :param W: 按低位优先的前W位排序
        """
        N = len(arr)
        R = 256
        aux = [str()] * N
        # 根据第d个字符用键索引计数法排序
        for d in range(W-1, -1, -1):
            # 计算出现频率
            count = [0] * (R + 1)
            for i in range(N):
                count[ord(arr[i][d]) + 1] += 1
            # 将频率转换为索引
            for r in range(R):
                count[r+1] += count[r]
            # 将元素分类
            for i in range(N):
                c = ord(arr[i][d])
                aux[count[c]] = arr[i]
                count[c] += 1
            # 回写
            for i in range(N):
                arr[i] = aux[i]


if __name__ == '__main__':
    arr = ["4PGC938", "4PGX938", "6GRE853", "4PGC915", "9ZHS314", "0SFR312", "1MAS120", "7SDX347", "5SUX888", "2KTU304", "5PFL366", "8IIG269"]
    # list_print(arr)
    sort = LSDSort()
    sort.sort(arr, 7)
    list_print(arr)