from collections import Counter
from math import log
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        count = Counter(deliciousness)
        pairs = 0
        for i in range(len(deliciousness)-1, -1, -1):
            if deliciousness[i]:
                l, r = log(deliciousness[i], 2), log(2*deliciousness[i], 2)
                count[deliciousness[i]] -= 1         
                if int(l) != int(r):
                    # print(deliciousness[i], pow(2, int(r))-deliciousness[i], count)
                    pairs += count[pow(2, int(r))-deliciousness[i]]
                    pairs += count[pow(2, int(l))-deliciousness[i]]
        return pairs % 1_000_000_007
                
            