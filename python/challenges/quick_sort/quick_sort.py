def QuickSort(arr, left, right):
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)

def Partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range (left , right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


temp = [8,4,23,42,16,15]
Reverse_sorted= [20,18,12,8,5,-2]
Few_uniques= [5,12,7,5,5,7]
Nearly_sorted= [2,3,5,7,13,11]
QuickSort(temp, 0 ,len(temp)-1)
QuickSort(Reverse_sorted, 0 ,len(Reverse_sorted)-1)
QuickSort(Few_uniques, 0 ,len(Few_uniques)-1)
QuickSort(Nearly_sorted, 0 ,len(Nearly_sorted)-1)
print(temp)
print(Reverse_sorted)
print(Few_uniques)
print(Nearly_sorted)
