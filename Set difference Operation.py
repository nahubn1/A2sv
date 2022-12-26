# Enter your code here. Read input from STDIN. Print output to STDOUT
nE = int(input())
setE = set(input().split(' '))
nF = int(input())
setF = set(input().split(' '))

print(len(setE.difference(setF)))
