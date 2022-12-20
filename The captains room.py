# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
rooms = list(map(int, input().split()))
count = Counter(rooms)
for room in count:
    if count[room] == 1:
        print(room)
