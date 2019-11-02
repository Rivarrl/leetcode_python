from typing import List

from algorithm_utils import *

def transformArray(arr: List[int]) -> List[int]:
    """
    首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。
    第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：
    假如一个元素小于它的左右邻居，那么该元素自增 1。
    假如一个元素大于它的左右邻居，那么该元素自减 1。
    首、尾元素 永不 改变。
    过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。
    示例 1：
    输入：[6,2,3,4]
    输出：[6,3,3,4]
    解释：
    第一天，数组从 [6,2,3,4] 变为 [6,3,3,4]。
    无法再对该数组进行更多操作。
    示例 2：
    输入：[1,6,3,4,3,5]
    输出：[1,4,4,4,4,5]
    解释：
    第一天，数组从 [1,6,3,4,3,5] 变为 [1,5,4,3,4,5]。
    第二天，数组从 [1,5,4,3,4,5] 变为 [1,4,4,4,4,5]。
    无法再对该数组进行更多操作。
    提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 100
    """
    n = len(arr)
    arr2 = [e for e in arr]
    def change(arr, arr2):
        for i in range(1, n-1):
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                arr2[i] += 1
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                arr2[i] -= 1
    change(arr, arr2)
    while arr2 != arr:
        arr = arr2[:]
        change(arr, arr2)
    return arr


if __name__ == '__main__':
    res = transformArray([6,5,8,6,7,7,3,9,8,8,3,1,2,9,8,3])
    print(res)
    pass