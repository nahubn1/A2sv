class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        que = deque(tickets)
        time = 0
        while que[k%n] > 0:
            left = que.popleft()-1            
            que.append(left)   
            k -= 1
            time += left >= 0
            
        return time