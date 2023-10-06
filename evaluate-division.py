class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        ratio = defaultdict(lambda: -1)
        
        variables = set()
        for (u, v), val in zip(equations, values):
            variables.add(u)
            variables.add(v)

            ratio[(u, u)] = ratio[(v, v)] = 1
            ratio[(u, v)] = val
            ratio[(v, u)] = 1/val
        

        for c in variables:
            for a in variables:
                for b in variables:
                    if ratio[(a, c)] != -1 and ratio[(b, c)] != -1:
                        ratio[(a, b)] = ratio[(a, c)] / ratio[(b, c)]
        
        ans = []
        for u, v in queries:
            ans.append(ratio[(u, v)])
        
        return ans