import unittest
# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    merged_arr = [0 for i in range(len(arrA) + len(arrB))]
    l_index, r_index, merged_index = 0, 0, 0
    while l_index < len(arrA) or r_index < len(arrB):
        # print("ARRA", len(arrA), arrA)
        # print("ARRB", len(arrB), arrB)
        if r_index == len(arrB) and l_index < len(arrA) and l_index != len(arrA) - 1:
            r_index -= 1
        if r_index == len(arrB):
            merged_arr[merged_index] = arrA[l_index]
            return merged_arr
        if l_index == len(arrA) or arrA[l_index] > arrB[r_index]:
            # print("RIGHT LIST", len(arrB), r_index)
            merged_arr[merged_index] = arrB[r_index]
            # print("RLIST", len(arrB), "INDEX", r_index)
            r_index += 1
            merged_index += 1
        else:
            merged_arr[merged_index] = arrA[l_index]
            l_index += 1
            merged_index += 1
    # print("MERGE", merged_arr)
    return merged_arr


# merge([1, 2, 7], [3, 5])

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


# merge_sort([1, 4, 7, 9, 2, 3, 5, 8])
# merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
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
