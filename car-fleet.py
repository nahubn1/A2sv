class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        
        fleet = 1
        for i in range(len(cars)-1, -1, -1):
            x0, v0 = cars[i-1]
            xi, vi = cars[i]
            
            if x0*vi - xi*v0 >= target*(vi-v0):
                cars[i-1] = cars[i]
            else:
                fleet += 1
                
        
        return fleet