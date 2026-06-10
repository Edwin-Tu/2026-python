"""Sorting algorithms for Stage 2."""


def bubble_sort(data: list) -> list:
    result = data[:]
    length = len(result)

    for end in range(length - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break

    return result


def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data[:]

    pivot = data[len(data) // 2]
    smaller = []
    equal = []
    greater = []

    for value in data:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(greater)


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data[:]

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
