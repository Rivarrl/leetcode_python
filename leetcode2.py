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


if __name__ == "__main__":
    r = counting_nums(8)
    print(r)
