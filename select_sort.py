# 选择排序是一种简单直观的排序算法，它也是一种交换排序算法，和冒泡排序有一定的相似度，可以认为选择排序是冒泡排序的一种改进。
# 稳定性：用数组实现的选择排序是不稳定的，用链表实现的选择排序是稳定的。
# 时间复杂度：O(n^2)，空间复杂度：O(1)


def select_sort(array):
    n = len(array)

    # 遍历所有数组元素
    for i in range(n):

        min_index = i

        # Last i elements are already in place
        for j in range(i + 1, n - i):

            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)


arr = [64, 34, 25, 12, 22, 11, 90]
select_sort(arr)
# [11, 12, 22, 34, 25, 64, 90]
