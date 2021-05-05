if __name__ == "__main__":
    riddle_index = 0

def binary_search_tree(arr,n) :

    if len(arr)==0:
        # print("Not Found")
        return False

    elif (not all(isinstance(i, int) for i in arr)) or type(n)!=int:
        # print("Type Error")
        return "Type Error"

    elif len(arr)==1:
        if arr[0]==n:
            # print("Found")
            return True
        else :
            # print("not Found")
            return False

    elif middle(arr)==n:
        # print("Found")
        return True

    elif middle(arr)>n:
        # print(arr[:len(arr)//2:])
        binary_search_tree(arr[:len(arr)//2:],n)

    elif middle(arr)<n:
        # print(arr[len(arr)//2::])
        binary_search_tree(arr[len(arr)//2::],n)

    else :
        # print("Not Found")
        return  False


def middle(array):
    return array[len(array)//2]

# a=[1,2,3,4,5,7,10,15,20,30]

# print(binary_search_tree([21],21))
# binary_search_tree(a,2)
# binary_search_tree(a,3)
# binary_search_tree(a,4)
# binary_search_tree(a,5)
# binary_search_tree(a,7)

# binary_search_tree(a,10)
# binary_search_tree(a,15)
# binary_search_tree(a,20)
# binary_search_tree(a,30)
