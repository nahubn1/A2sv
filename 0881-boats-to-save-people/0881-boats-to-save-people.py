class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        ptr1 = 0
        ptr2 =  len(people) - 1        
        
        fats = 0
        thins = 0
        
        while ptr1 <= ptr2:
            if ptr1 == ptr2:
                fats += 1
                break
                
            if people[ptr1] + people[ptr2] <= limit:
                thins += 2
                ptr1 += 1
                ptr2 -= 1
            else:
                fats += 1
                ptr2 -= 1
                
        return fats+int(thins/2)