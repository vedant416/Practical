def partition(array, start, end):
    
    pivotIndex = start # actual index
    pivot = array[end] # temp assign pivot to end
    
    for i in range(start, end):
        if array[i] < pivot:
            array[pivotIndex], array[i] = array[i], array[pivotIndex]
            pivotIndex = pivotIndex + 1

    array[pivotIndex], array[end] = array[end], array[pivotIndex]

    return pivotIndex


def quickSort(array, start, end):
    if start < end:
        pi = partition(array, start, end)
        quickSort(array, start, pi - 1)
        quickSort(array, pi + 1, end)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array:")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
