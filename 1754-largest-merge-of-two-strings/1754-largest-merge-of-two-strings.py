class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        
        ptr1, ptr2 = 0, 0
        merge = []
        while ptr1 < l1 and ptr2 < l2:
            if ord(word1[ptr1]) > ord(word2[ptr2]):
                merge.append(word1[ptr1])
                ptr1 += 1
                
            elif ord(word1[ptr1]) == ord(word2[ptr2]):
                if word1[ptr1:] > word2[ptr2:]:
                    merge.append(word1[ptr1])
                    ptr1 += 1
                else:
                    merge.append(word2[ptr2])
                    ptr2 += 1
            else:
                merge.append(word2[ptr2])
                ptr2 += 1
                
        merge.extend(list(word1)[ptr1:])
        merge.extend(list(word2)[ptr2:])
        
        return  "".join(merge)
        