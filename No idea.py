# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m  = input().split(' ')
nums = list(input().split(' '))
A = set(input().split(' '))
B = set(input().split(' '))
happines = 0
for num in nums:
    if num in A:
        happines += 1
    elif num in B:
        happines -= 1
print(happines)
