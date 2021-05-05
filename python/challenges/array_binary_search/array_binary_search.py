if __name__ == "__main__":
    riddle_index = 0

def binary_search(arr,n) :

    if len(arr)==0:
        # print("Not Found")
        return -1

    elif (not all(isinstance(i, int) for i in arr)) or type(n)!=int:
        # print("Type Error")
        return "Type Error"

    elif len(arr)==1:
        if arr[0]==n:
            return True
        else :
            return -1

    elif middle(arr)==n:
        return True

    elif middle(arr)>n:
        # print(arr[:len(arr)//2:])

        return binary_search(arr[:len(arr)//2:],n)

    elif middle(arr)<n:
        # print(arr[len(arr)//2::])
        return binary_search(arr[len(arr)//2::],n)

    else :
        # print("Not Found")
        return  -1


def middle(array):
    return array[len(array)//2]

a=[1,2,3,4,5,7,10,15,20,30]

# print(binary_search([21],21))
print(binary_search(a,2))
print(binary_search(a,3))
print(binary_search(a,4))
print(binary_search(a,5))
# binary_search(a,7)

# binary_search(a,10)
# binary_search(a,15)
# binary_search(a,20)
# binary_search(a,30)
