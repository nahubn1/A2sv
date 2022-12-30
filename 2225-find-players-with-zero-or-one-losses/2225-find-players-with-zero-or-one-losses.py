from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        games = Counter([])
        points = Counter([])
        for team1, team2 in matches:
            games[team1] += 1 
            games[team2] += 1
            points[team1] += 1
            
        no_lose = []
        one_lose = []
        for team in games:
            if points[team] == games[team]:
                no_lose.append(team)
            elif points[team] == games[team]-1:
                one_lose.append(team)
        return [sorted(no_lose), sorted(one_lose)]