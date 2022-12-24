class Solution:
    def multiply(self, num1: str, num2: str) -> str:
#         expanded1 = []
#         for i in range(len(num1)):
#             expanded1.append((num1[i], pow(10, len(num1)-i-1)))
        
#         expanded2 = []
#         for i in range(len(num2)):
#             expanded2.append((num2[i], pow(10, len(num2)-i-1)))
            
#         res = 0
#         for i1, multiplier1 in expanded1:
#             for i2, multiplier2 in expanded2:
#                 res += ((int(i1)*int(i2))*int(multiplier1)*int(multiplier2))
#         return str(res)
            return str(int(num1)*int(num2))