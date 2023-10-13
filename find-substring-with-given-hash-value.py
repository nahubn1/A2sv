class Solution:
    def subStrHash(self, s: str, power: int, mod: int, k: int, hashValue: int) -> str:
        modAdd = lambda num1, num2, mod: ((num1 % mod) + (num2 % mod))%mod
        modSubs = lambda num1, num2, mod: ((num1 % mod) - (num2 % mod))%mod
        modMul = lambda num1, num2, mod: ((num1 % mod) * (num2 % mod))%mod
        n = len(s)

        val = lambda char: ord(char) - 96
        Pow = pow(power, k, mod)
        print(Pow)
        ans = ''
        window = 0
        for i in range(n-1, -1, -1):
            window = modMul(window, power, mod)
            window = modAdd(window, val(s[i]), mod)
            if i <= n-k:
                if i < n-k: 
                    window = modSubs(window, modMul(val(s[i+k]), Pow, mod), mod)

                if window == hashValue:
                    ans = s[i:i+k]
            
        
        return ans