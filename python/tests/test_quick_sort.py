from challenges.quick_sort.quick_sort import quick_sort

def test_insertion_sort():
    userinput = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    quick_sort(userinput)
    assert userinput == expected

def test_insertionSort2():
    userinput = [20, 41, 3, 2, 16, 10]
    expected = [2, 3, 10, 16, 20, 41]
    quick_sort(userinput)
    assert userinput == expected
