class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        primes = [1]*n

        primes[0] = primes[1] = 0

        for i in range(n):
            if primes[i]:
                mul = i
                while mul + i < n:
                    primes[mul+i] = 0
                    mul += i
        
        
        return primes.count(1)