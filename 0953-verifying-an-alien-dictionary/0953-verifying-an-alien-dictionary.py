class Solution:
    @staticmethod
    def correct(word1, word2, alphabet):
        minLen = min(len(word1), len(word2))
        
        for i in range(minLen):
            # print(alphabet[word1[i]] < alphabet[word2[i]])
            if alphabet[word1[i]] < alphabet[word2[i]]: 
                # print('here')
                return True
            elif alphabet[word1[i]] > alphabet[word2[i]]: 
                # print('here2')
                return False
        else: return True if len(word1) <= len(word2) else False
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {order[i]: i+1 for i in range(len(order))}
        # print(self.correct(words[0], words[1], alphabet))
        for i in range(len(words)-1):
            if not self.correct(words[i], words[i+1], alphabet):
                 return False
        else: return True
                    
            
            