from challenges.quick_sort.quick_sort import QuickSort

def test_insertion_sort():
    userinput = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    QuickSort(userinput, 0 ,len(userinput)-1)
    assert userinput == expected

def test_insertionSort2():
    userinput = [20, 41, 3, 2, 16, 10]
    expected = [2, 3, 10, 16, 20, 41]
    QuickSort(userinput, 0 ,len(userinput)-1)
    assert userinput == expected

