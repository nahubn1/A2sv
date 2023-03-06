class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.n = len(persons)
        self.times = times
        self.voteCount = defaultdict(int)
        self.leading = []
        for person in persons:
            self.voteCount[person] += 1
            if self.leading:
                if self.voteCount[person] >= self.voteCount[self.leading[-1]]:
                    self.leading.append(person)
                else:
                    self.leading.append(self.leading[-1])
            else:
                self.leading.append(person)
        

    def q(self, t: int) -> int:
        start, end = 0, self.n-1
        while start<=end:
            middle = (start+end)//2
            if self.times[middle] <= t:
                start = middle + 1
            else:
                end = middle - 1

        return self.leading[start-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)