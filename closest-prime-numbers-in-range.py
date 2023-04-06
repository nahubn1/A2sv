class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True]*(right+1)
        is_prime[0] = is_prime[1] = False
        for i in range(ceil(sqrt(right))+1):
            if is_prime[i]:
                for j in range(2*i, right+1, i):
                    is_prime[j] = False
        
        res = [-1, -1]
        start = left
        while res[1] == -1:
            if start > right:
                return [-1, -1]

            if is_prime[start]:
                if res[0] == -1:
                    res[0] = start
                else:
                    res[1] = start
                    
            start += 1


        prev = res[1]
        for i in range(start, right+1):
            if is_prime[i]:
                if i-prev < res[1]-res[0]:
                    res = [prev, i]
                prev = i

        return res