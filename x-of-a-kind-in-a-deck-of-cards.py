class Solution:
    def gcf(self, a, b):
        if b == 0:
            return a

        return self.gcf(b, a%b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = set(Counter(deck).values())
        all_gcf = 0
        for c in count:
            all_gcf = self.gcf(all_gcf, c)

        return all_gcf != 1