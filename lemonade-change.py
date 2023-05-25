class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens, fives = 0, 0
        for bill in bills:
            if bill == 5: fives += 1
            if bill == 10: tens += 1

            change = bill-5
            while change:
                if change > 10 and tens > 0:
                    tens -= 1
                    change -= 10
                elif fives:
                    fives -= 1
                    change -= 5
                else:
                    return False
        
        return True