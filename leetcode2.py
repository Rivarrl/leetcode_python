# -*-coding:utf-8-*-
# leetcode.py 内容太杂了，新起一个leetcode2.py

# 数数字，1->11->21->1211->.....
# 1 -> 11(1个1)
# 11 -> 21(2个1)
def counting_nums(t):
    def inner(num):
        l = num.__len__()
        res = ""
        i = 0
        while i < l:
            j = i
            count = 0
            while num[j] == num[i]:
                j += 1
                count += 1
                if j == l:
                    break
            res += str(count) + num[i]
            i = j
        return res

    result = "1"
    for _ in range(t - 1):
        result = inner(result)
    return result


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = nums.__len__()
    if l <= 1:
        return l
    i = 0
    while i < l - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i + 1])
            l -= 1
        else:
            i += 1
    return l


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    ls = str.strip('"').lstrip()
    i, k = 0, 0
    if ls.__len__() == 0 or (ls.__len__() == 1 and ls[0] == '-'):
        return 0
    try:
        _ = int(ls[0])
    except:
        if ls[0] == '-':
            i, k = 1, 1
        elif ls[0] == '+':
            i, k = 1, 2
        else:
            return 0
    while i < ls.__len__():
        if isint(ls[i]):
            i += 1
        else:
            # i -= 1
            break
    if i == 0:
        if k == 1 or k == 2:
            return 0
        else:
            return int(ls[0])
    res = ls[1:i] if k == 2 else ls[:i]
    if isint(res):
        if int(res) < int_min:
            return int_min
        elif int(res) > int_max:
            return int_max
        else:
            if res.rstrip('0') == '-':
                return 0
            return int(res)
    return 0


def isint(i):
    try:
        _ = int(i)
        return True
    except:
        return False


if __name__ == "__main__":
    r = counting_nums(8)
    print(r)
