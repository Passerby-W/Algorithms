# 和归并类似，快速排序的基本思想也是分治法。
# 不稳定
# 时间复杂度：情况下可以做到O(nlogn)，极端情况下才会退化O(n^2)，可以通过随机pivot改进。空间复杂度：平均O(logn)，最坏O(n)
import random


def quick_sort(array, left, right):
    if left >= right:
        return array
    q = partition(array, left, right)
    quick_sort(array, left, q - 1)
    quick_sort(array, q + 1, right)
    return array


def partition(array, left, right):
    pivot = random.randint(left, right)
    array[pivot], array[right] = array[right], array[pivot]
    i = left
    for j in range(left, right):
        if array[j] <= array[right]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]
    return i


arr = [64, 34, 25, 12, 22, 11, 90]
l, r = 0, len(arr) - 1
print(quick_sort(arr, l, r))
# [11, 12, 22, 34, 25, 64, 90]
