# 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

# 冒泡排序的时间复杂度为 O(n^2)，空间复杂度：O(1)
# 在相邻元素相等时，它们并不会交换位置，所以，冒泡排序是稳定排序。


def bubble_sort(array):
    n = len(array)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)


def better_bubble_sort(array):
    n = len(array)

    # 遍历所有数组元素
    for i in range(n):
        swap = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True

        if not swap:
            break
    print(array)


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
better_bubble_sort(arr)
# [11, 12, 22, 25, 34, 64, 90]
# [11, 12, 22, 25, 34, 64, 90]
