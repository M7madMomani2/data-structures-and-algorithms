def multi_bracket_validation(strings):

    arr = []
    key_rule = { '(':')', '[':']', '{':'}' }

    for x in strings:
        if (x == '(' or x == '{' or x == '['):
            arr.append(x)
        elif x in key_rule.values():
            if len(arr) == 0:
                return False
            item = arr.pop()
            if x != key_rule[item]:
                return False

    if len(arr) != 0:
        return False

    return True

