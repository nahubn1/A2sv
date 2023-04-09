"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {}
        for emp in employees:
            hashmap[emp.id] = emp
        
        def total_imp(emp):
            if not emp:
                return 0

            imp = emp.importance
            for sub in emp.subordinates:
                imp += total_imp(hashmap[sub])
            
            return imp

        return total_imp(hashmap[id])