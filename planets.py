from collections import Counter

tests = int(input())

for i in range(len(tests)):
    cost = 0
    n, c = map(int, input().split())
    planets = list(map(int, input().split()))
    count = Counter(planets)
    for planet in count:
        cost += min(count[planet], c)
    print(cost)
