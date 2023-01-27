class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        ptr1, ptr2 = 0, 0
        match = 0
        while ptr1 < len(players) and ptr2 < len(trainers):
            
            if players[ptr1] <= trainers[ptr2]:
                match += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
                
        return match