class Solution:
    def lengthOfLongestSubstring(self, s):
        Set = set()
        start, end = 0, 0
        longest = 0
        for end in range(len(s)):
            
            while s[end] in Set:
                Set.remove(s[start])
                start += 1

            Set.add(s[end])

            longest = max(longest, end-start+1)

        return longest
                