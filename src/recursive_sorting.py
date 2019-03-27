# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    l_index, r_index = 0, 0
    while l_index < len(arrA) or r_index < len(arrB):
        if l_index == len(arrA) or arrA[l_index] > arrB[r_index]:
            merged_arr.append(arrB[r_index])
            r_index += 1
        else:
            merged_arr.append(arrA[l_index])
            l_index += 1

    print("MERGED", merged_arr)
    return merged_arr


merge([1, 2], [2, 3])

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


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
