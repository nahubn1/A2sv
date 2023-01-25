class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_instance = {s[i]: i for i in range(len(s))}
        win_len, max_last_instance, res = 0, 0, []
        for i in range(len(s)):
            max_last_instance = max(max_last_instance, last_instance[s[i]])
            win_len += 1
            if i == max_last_instance:
                res.append(win_len)
                win_len = 0
        return res