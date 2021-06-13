def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j+1] = key


list1 = [8,4,23,42,16,15]
list2 = [20,18,12,8,5,-2]
list3 = [5,12,7,5,5,7]
list4 = [2,3,5,7,13,11]

InsertionSort(list1)
InsertionSort(list2)
InsertionSort(list3)
InsertionSort(list4)
print(list1)
print(list2)
print(list3)
print(list4)
