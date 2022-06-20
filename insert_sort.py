# 插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 稳定
# 时间复杂度：O(n^2)，空间复杂度：O(1)


def insert_sort(array):
    n = len(array)

    for i in range(1, n):

        value = array[i]

        j = i

        while j > 0 and array[j - 1] > value:

            array[j] = array[j - 1]

            j -= 1

        array[j] = value

    print(array)


arr = [64, 34, 25, 12, 22, 11, 90]
insert_sort(arr)
# [11, 12, 22, 34, 25, 64, 90]
