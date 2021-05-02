
# USERINPUT = LIST
if __name__ == "__main__":
    riddle_index = 0


def reverseCheck(userInput):
    newArr = []
    if type(userInput)==list:
        for i in range(len(userInput)) :
            newArr.append(userInput.pop())
        return newArr
    else:
        return False


