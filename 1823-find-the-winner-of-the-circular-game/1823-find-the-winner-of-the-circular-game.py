from math import floor
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        start_i = 0
        players = list(range(1, n+1))
        while len(players) > 1:
            loser_i =  start_i+k - len(players)*floor(((start_i+k-1)/len(players))) - 1
            # print('Players =', players, 'start_i =', start_i, 'loser_i =', loser_i)
            players.pop(loser_i)
            start_i = loser_i  - len(players)*floor(loser_i/len(players))
        return players[0]