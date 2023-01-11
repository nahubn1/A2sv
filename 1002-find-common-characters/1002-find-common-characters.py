class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = set(words[0])
        ans = []
        for letter in letters:
            minn = words[0].count(letter)
            for word in words:
                if word.count(letter) == 0:
                    break
                minn = min(word.count(letter), minn)
            else:
                ans.extend([letter]*minn)
                
        return ans