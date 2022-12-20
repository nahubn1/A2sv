# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
words = [input() for i in range(n)]
count = Counter(words)
l2 = ''
for i in count.values():
    l2 += f'{i} '
print(len(count.values()))
print(l2)
