# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    al = len(arrA)
    bl = len(arrB)
    f = 0
    g = 0
    h = 0
    while f < al and g < bl:
        if arrA[f] < arrB[g]:
            merged_arr[h] = arrA[f]
            f += 1
            h += 1
        else:
            merged_arr[h] = arrB[g]
            g += 1
            h += 1

    while f < al:
        merged_arr[h] = arrA[f]
        f += 1
        h += 1

    while g < bl:
        merged_arr[h] = arrB[g]
        g += 1
        h += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    A = arr[:len(arr)//2]
    B = arr[len(arr)//2:]

    if len(A) > 1 or len(B) > 1:
        A = merge_sort(A)
        B = merge_sort(B)

    return merge(B, A)


print(merge_sort([9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]))


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
