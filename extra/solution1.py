def question1(arr):
    """
    数字键盘按键
    1234567890
    操作有：按下、左移和右移
    初始左右手分别在5和6的位置，问敲出给定序列的最小操作次数
    :param arr: List[int]
    :return: int
    """
    def dfs(i, j, k, cur):
        if k == n:
            ans[0] = min(ans[0], cur)
            return
        if (j != 0 and arr[k] >= j) or arr[k] == 0:
            dfs(i, arr[k], k + 1, cur + arr[k] - j)
        elif arr[k] <= i:
            dfs(arr[k], j, k + 1, cur + i - arr[k])
        else:
            dfs(i, arr[k], k + 1, cur + j - arr[k])
            dfs(arr[k], j, k + 1, cur + arr[k] - i)

    n = len(arr)
    ans = [float("inf")]
    dfs(5, 6, 0, n)
    print(ans[0])
    return ans[0]


def question2(arr):
    """
    交换产生最大的数
    如：1,3,2 -> 3,1,2
    4, 6, 7, 1 -> 7, 6, 4, 1
    :param arr: List[int]
    :return: List[int]
    """
    a = arr[:]
    print(a)
    N = len(arr)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(i):
        left = i * 2 + 1
        right = left + 1
        root = i
        if left < N and arr[left] > arr[root]:
            root = left
        if right < N and arr[right] > arr[root]:
            root = right
        if root != i:
            swap(arr, i, root)
            heapify(root)

    for i in range(len(arr) // 2, -1, -1):
        heapify(i)

    j = 0
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, i, 0)
        if a[j] != arr[i]:
            k = a.index(arr[i])
            swap(a, k, j)
            break
        N -= 1
        j += 1
        heapify(0)
    print(a)
    return a


if __name__ == '__main__':
    question1([9,6,7,1,7])
    question2([8, 7, 6, 5, 4, 2, 3, 1])
    pass
