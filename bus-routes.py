class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        graph = defaultdict(set)
        routes = [set(route) for route in routes]

        city_buses = defaultdict(list)

        for i in range(len(routes)):
            for city in routes[i]:
                city_buses[city].append(i)
            
        graph = defaultdict(list)
        for city in city_buses:
            arr = city_buses[city]
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    graph[arr[i]].append(arr[j])
                    graph[arr[j]].append(arr[i])
        
        que = deque(city_buses[source])
        visited = set(city_buses[source])
        step = 1
        while que:
            for _ in range(len(que)):
                bus = que.popleft()
                if target in  routes[bus]:
                    return step

                for neighbor in graph[bus]:
                    if neighbor not in visited:
                        que.append(neighbor)
                        visited.add(neighbor)
                
            step += 1
        
        
        return -1