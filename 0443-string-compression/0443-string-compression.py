class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ptr = 0
        while ptr < len(chars):
            char = chars[ptr]
            count=1
            ptr += 1
            while ptr < len(chars) and chars[ptr] == char:
                chars.pop(ptr)
                count += 1
                
            count = str(count) if count > 1 else ""
            for i in count:
                chars.insert(ptr, i)
                ptr += 1
                
        
        return len(chars)
                
                
        
        
                
        
              
        