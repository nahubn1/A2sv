class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, [enTime, pTime] in enumerate(tasks):
            tasks[i] = (pTime, i, enTime)

        tasks.sort(key = lambda x: x[2])

        heap = []
        ans = []

        ptr = 0
        time = 0
        while ptr < len(tasks) or heap:
            if heap:
                proc_time, index, enq_time = heappop(heap)
                ans.append(index)
                
                time += proc_time
                while ptr < len(tasks) and tasks[ptr][2] <= time:
                    heappush(heap, (tasks[ptr]))
                    ptr += 1
            else:
                time = tasks[ptr][2]
                while ptr < len(tasks) and tasks[ptr][2] == time:
                    heappush(heap, tasks[ptr])
                    ptr += 1
            
        return ans