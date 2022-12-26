import textwrap

def wrap(string, max_width):
    res = []
    for i in range(len(string)):
        if i and i%max_width == 0:
            res.append('\n')
        res.append(string[i])
    
    return ''.join(res)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
