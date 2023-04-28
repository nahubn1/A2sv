class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        unlocked = [False]*len(rooms)
        keys = deque([0])

        while keys:
            key = keys.popleft()
            unlocked[key] = True

            for newKey in rooms[key]:
                if not unlocked[newKey]:
                    keys.append(newKey)
        
        return all(unlocked)