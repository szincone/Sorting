import unittest


def merge(arrA, arrB):
    merged_arr = [0 for i in range(len(arrA) + len(arrB))]
    l_index, r_index, merged_index = 0, 0, 0
    while l_index < len(arrA) or r_index < len(arrB):
        if r_index == len(arrB) and l_index < len(arrA) and l_index != len(arrA) - 1:
            r_index -= 1
        if r_index == len(arrB):
            merged_arr[merged_index] = arrA[l_index]
            return merged_arr
        if l_index == len(arrA) or arrA[l_index] > arrB[r_index]:
            merged_arr[merged_index] = arrB[r_index]
            r_index += 1
            merged_index += 1
        else:
            merged_arr[merged_index] = arrA[l_index]
            l_index += 1
            merged_index += 1
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


if __name__ == '__main__':
    unittest.main()
