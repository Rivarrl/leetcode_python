# -*- coding: utf-8 -*-
# ======================================
# @File    : 384.py
# @Time    : 2019/12/20 22:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        sf = self.arr[:]
        for i in range(1, len(sf)):
            j = random.randint(0, i)
            if j != i:
                sf[i], sf[j] = sf[j], sf[i]
        return sf

if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    nums = [1,2,3]
    obj = Solution(nums)
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)
