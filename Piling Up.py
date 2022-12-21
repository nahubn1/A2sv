# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import inf
tests = int(input())
for i in range(tests):
    top  = inf
    n = int(input())
    cubes = list(map(int, input().split()))
    while cubes:
        comp = {0: cubes[0], -1: cubes[-1]}
        candidate = max(comp, key=comp.get)
        if top >= cubes[candidate]:
            top = cubes.pop(candidate)
        else:
            print('No')
            break
    else:
        print('Yes')
