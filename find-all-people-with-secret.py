class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for u, v, t in meetings:
            graph[u].append((v, t))
            graph[v].append((u, t)) 
        graph[0].append((firstPerson, 0))

        time = [inf]*n
        time[0] = -1
        heap = [(-1, 0)]
        listened = set()

        while heap:
            t, person = heappop(heap)

            if person in listened:
                continue

            time[person] = t
            listened.add(person)

            for friend, meet_time in graph[person]:
                
                if friend not in listened and meet_time >= t and time[friend] > meet_time:
                    heappush(heap, (meet_time, friend))
        

        time = [(t, p) for p, t in enumerate(time)]
        time.sort()

        ans = []
        for t, p in time:
            if t < inf:
                ans.append(p)
        
        return ans