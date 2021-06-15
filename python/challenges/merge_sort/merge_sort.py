
def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        Mergesort(left)
        Mergesort(right)
        Merge(left, right, arr)

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=  1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


temp = [8,4,23,42,16,15]
Reverse_sorted= [20,18,12,8,5,-2]
Few_uniques= [5,12,7,5,5,7]
Nearly_sorted= [2,3,5,7,13,11]
Mergesort(temp)
Mergesort(Reverse_sorted)
Mergesort(Few_uniques)
Mergesort(Nearly_sorted)
print(temp)
print(Reverse_sorted)
print(Few_uniques)
print(Nearly_sorted)
