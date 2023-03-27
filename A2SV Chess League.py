def find_winners(rating, k, s, e):
    winners = []
 
    if s + 1 == e:
        leftWinners = [s]
        rightWinners = [e]
    else:
        m = (s+e)//2
        leftWinners = sorted(find_winners(rating, k ,s, m))
        rightWinners = sorted(find_winners(rating, k, m+1, e))
    
    leftWeak = min(leftWinners, key=lambda x: rating[x])
    for player in rightWinners:
        if rating[leftWeak] - rating[player] <= k:
            winners.append(player)
    
    rightWeak = min(rightWinners, key=lambda x: rating[x])
    for player in leftWinners:
        if rating[rightWeak] - rating[player] <= k:
            winners.append(player)
    
    return winners
 
n, k = map(int, input().split())
scores = list(map(int, input().split()))
winners = sorted(find_winners(scores, k, 0, 2**n-1))
print(*[i+1 for i in winners])