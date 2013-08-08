# Implementation is merge sort with the augmentation that we count
# every time a number is merged across a number to the left of it

def merge_sort(a):
    if len(a) == 1:
        return a, 0

    mid = len(a) / 2
    left_merged, i1 = merge_sort(a[:mid])
    right_merged, i2  = merge_sort(a[mid:])
    sorted_arr, i3 = merge(left_merged, right_merged)
    return sorted_arr, (i1 + i2 + i3)


def merge(left, right):
    inversions = 0
    result = [0]*(len(right) + len(left))

    result_point = 0
    left_point = 0
    right_point = 0

    while left_point < len(left) and right_point < len(right):
        if left[left_point] < right[right_point]:
            result[result_point] = left[left_point]
            result_point += 1
            left_point += 1
        else:
            result[result_point] = right[right_point]
            result_point += 1
            right_point += 1
            inversions += len(left) - left_point

    while left_point < len(left):
        result[result_point] = left[left_point]
        result_point += 1
        left_point += 1

    while right_point < len(right):
        result[result_point] = right[right_point]
        result_point += 1
        right_point += 1

    return result, inversions

print merge_sort([int(num.strip()) for num in open('IntegerArray.txt')])[1]
