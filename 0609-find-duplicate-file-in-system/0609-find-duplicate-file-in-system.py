from collections import Counter
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contexts = {}
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                
                file, content = path[i].split('(')
                
                if content in contexts:
                    contexts[content].append(path[0]+'/'+file)
                else:
                    contexts[content] = [path[0]+'/'+file]
        
        duplicates = []
        for files in contexts.values():
            if len(files) > 1:
                duplicates.append(files)
                
        return duplicates
            
            
            