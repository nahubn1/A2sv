class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        canonical = []
        for p in path:
            if p != '':
                if canonical and p == '..':
                    canonical.pop()
                    
                elif p != '.' and p != '..':
                    canonical.append('/'+p)
                
        return ''.join(canonical) if canonical else '/'