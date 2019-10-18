from algorithm_utils import *

# leetcode困难题2

def numberToWords(num):
    """
    273. 整数转换英文表示
    将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
    示例 1:
    输入: 123
    输出: "One Hundred Twenty Three"
    示例 2:
    输入: 12345
    输出: "Twelve Thousand Three Hundred Forty Five"
    示例 3:
    输入: 1234567
    输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    示例 4:
    输入: 1234567891
    输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    :param num: int
    :return: str
    """
    twenty = " One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    ty = "  Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    hundred = "Hundred"
    unit = " Thousand Million Billion".split(' ')
    if num == 0: return "Zero"
    def recur(n, t):
        if n < 20:
            return [twenty[n], unit[t]]
        elif 20 <= n < 100:
            return [ty[n//10]] + recur(n%10, t)
        elif 100 <= n < 1000:
            return [twenty[n//100], hundred] + recur(n%100, t)
        else:
            return recur(n//1000, t+1) + recur(n%1000, t)
    res = [e for e in recur(num, 0) if e]
    j = len(res) - 1
    while j > 0:
        if res[j] in unit and res[j-1] in unit:
            res.pop(j)
        j -= 1
    print(res)
    return ' '.join(res)


if __name__ == '__main__':
    # numberToWords(1000)
    pass
