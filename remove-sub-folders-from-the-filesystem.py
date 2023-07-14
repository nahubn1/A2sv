class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x: len(x))

        mains = set()
        for path in folder:
            path = path.split('/')
            for i in range(len(path)):
                if tuple(path[:i+1]) in mains:
                    break
            else:
                mains.add(tuple(path))
        
        return ['/'.join(path) for path in mains]