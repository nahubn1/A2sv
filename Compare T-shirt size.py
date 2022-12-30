n = int(input())


def number_eqv(size):
    degree = len(size)
    mul = dict({'S': -1, 'M': 0, 'L': 1})[size]
    return degree * mul


for n in range(n):
    left, right = map(number_eqv, input().split())
    if left > right:
        print('>')
    elif left == right:
        print('=')
    else:
        print('<')
