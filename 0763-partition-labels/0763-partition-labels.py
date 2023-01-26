class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_instance = {s[i]: i for i in range(len(s))}
        part_limit = 0
        partitions = []
        start = 0
        for i in range(len(s)):
            part_limit = max(last_instance[s[i]], part_limit)
            if i == part_limit:
                partitions.append(part_limit-start+1)
                start = i + 1
        
        return partitions