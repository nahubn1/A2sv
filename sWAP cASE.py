def swap_case(s):
    stack = []
    for char in s:
        if char.isupper():
            stack.append(char.lower())
        else:
            stack.append(char.upper())
    return ''.join(stack)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
