# -*- coding: utf-8 -*-
# ======================================
# @File    : 1146.py
# @Time    : 2019/12/3 0:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_list = [{0: 0} for _ in range(length)]
        self.snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        self.snap_list[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 存在就直接返回
        if snap_id in self.snap_list[index]: return self.snap_list[index][snap_id]
        # 不存在就找第一个比它小的数
        s_list = list(self.snap_list[index].keys())
        lo, hi = 0, len(s_list)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if s_list[mid] < snap_id:
                lo = mid + 1
            else:
                hi = mid
        return self.snap_list[index][s_list[lo-1]]

if __name__ == '__main__':
    a = SnapshotArray(4)
    a.snap()
    a.snap()
    x = a.get(3, 1)
    print(x)
    a.set(2, 4)
    a.snap()
    a.set(1, 4)
    a.snap()
    print(a.snap_list)
    x = a.get(3, 0)
    print(x)
