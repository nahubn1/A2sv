class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)

        def bfs():
            que = deque([beginWord])
            visited = set()
            parents = defaultdict(set)

            visited_level = set([beginWord])
            while que:
                lev_len = len(que)
                visited = visited.union(visited_level)
                visited_level.clear()
                for _ in range(lev_len):

                    word = que.popleft()
                    if word == endWord:
                        return parents

                    for i in range(len(word)):
                        for j in range(26):
                            newWord = word[:i] + chr(97 + (ord(word[i]) - 97 + j)%26) + word[i+1:]
                            if newWord in wordList and newWord not in visited:
                                que.append(newWord)
                                parents[newWord].add(word)
                                visited_level.add(newWord)
            
            return parents
        

        parents = bfs()
        if not parents[endWord]:
            return []

        def dfs(node):
            if not parents[node]:
                return [[node]]

            transformations = []
            for p in parents[node]:
                trans = dfs(p)
                for tran in trans:
                    tran.append(node)
                    transformations.append(tran)

            return transformations
        
        return dfs(endWord)