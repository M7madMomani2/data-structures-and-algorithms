from challenges.merge_sort.merge_sort import Merge ,Mergesort

def test_insertion_sort():
    userinput = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    Mergesort(userinput)
    assert userinput == expected

def test_insertionSort2():
    userinput = [20, 41, 3, 2, 16, 10]
    expected = [2, 3, 10, 16, 20, 41]
    Mergesort(userinput)
    assert userinput == expected
