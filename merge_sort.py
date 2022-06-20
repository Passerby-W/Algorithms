# 归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用。
# 稳定
# 时间复杂度：复杂度为O(nlogn)，空间复杂度为O(n)


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2

    left = array[:mid]

    right = array[mid:]

    return marge(merge_sort(left), merge_sort(right))


def marge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))
# [11, 12, 22, 34, 25, 64, 90]
