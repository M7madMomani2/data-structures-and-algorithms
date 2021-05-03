
if __name__ == "__main__":
    riddle_index = 0



# **********solution 1 using math(ceil)*********
# import math
# def insertShiftArray(arr, val):
#     arrLength= math.ceil(len(arr)/2)
#     return(arr[:arrLength] + [val] + arr[arrLength:])

def insertShiftArray(arr,val):
    arrLength=len(arr)
    if not arrLength%2:
        return(arr[:(arrLength//2)] + [val] + arr[(arrLength//2):])
    else:
        return(arr[:arrLength//2+1] + [val] + arr[arrLength//2+1:])


def removeShiftArray(arr):
    arrLength=len(arr)
    if not arrLength%2:
        return(arr[:(arrLength//2)] + arr[(arrLength//2+1):])
    else:
        return(arr[:arrLength//2] + arr[arrLength//2+1:])


hola=[1, 2, 3, 4, 5]
print(f"before insert  {hola}")
hola =removeShiftArray(hola)
print(f"after remove  {hola}")
hola =insertShiftArray(hola, 10)
print(f"after insert  {hola}")
