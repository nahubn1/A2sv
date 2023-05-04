class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        count = Counter(words)
        for word in count:
            heap.append((-count[word], word))
            
        heapify(heap)

        ans = []
        while len(ans) < k:
            ans.append(heappop(heap)[1])
        
        return ans