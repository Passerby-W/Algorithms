# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
# 希尔排序是非稳定排序算法。
# 时间复杂度：O(nlogn)，空间复杂度：O(1)


def shell_sort(array):
    n = len(array)

    gap = n // 2

    while gap > 0:

        for i in range(1, n):

            value = array[i]

            j = i

            while j > 0 and array[j - 1] > value:

                array[j] = array[j - 1]

                j -= 1

            array[j] = value

        gap = gap // 2

    print(array)


arr = [64, 34, 25, 12, 22, 11, 90]
shell_sort(arr)
# [11, 12, 22, 34, 25, 64, 90]
