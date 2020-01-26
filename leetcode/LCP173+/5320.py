# -*- coding: utf-8 -*-
# ======================================
# @File    : 5320.py
# @Time    : 2020/1/26 10:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """

    """
    @timeit
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if veganFriendly == 1:
            restaurants = [[i, r, v, p, d] for i, r, v, p, d in restaurants if v == 1]
        restaurants = sorted([[i, r, v, p, d] for i, r, v, p, d in restaurants if p <= maxPrice and d <= maxDistance], key=lambda x: (x[1], -x[3], -x[4]), reverse=True)
        return [i for i, r, v, p, d in restaurants]


if __name__ == '__main__':
    a = Solution()
    a.filterRestaurants(restaurants=[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10)
    a.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10)
    a.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3)