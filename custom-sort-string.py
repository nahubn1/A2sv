class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alphabet = defaultdict(lambda:-1)
        for i in range(len(order)):
            alphabet[order[i]] = i
        
        ans = sorted(s, key = lambda x:alphabet[x])
        return ''.join(ans)