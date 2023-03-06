class Solution:
    @staticmethod
    def f(string):
        return string.count(min(string))

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(words)
        words = [self.f(word) for word in words]
        words.sort()
        ans = []
        for query in queries:
            start, end = 0, n-1
            target = self.f(query)
            while start <= end:
                middle = (start+end)//2
                if words[middle] <= target:
                    start = middle + 1
                else:
                    end = middle - 1
            
            ans.append(n-start)

        return ans