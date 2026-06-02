class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =="0" or num2 == "0":
            return "0"

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        n, m = len(num1), len(num2)
        
        res = [0] * (n+m)

        for i in range(n-1, -1, -1):
            d1 = ord(num1[i]) - ord("0")
            for j in range(m-1, -1, -1):
                d2 = ord(num2[j]) - ord("0")

                mul = d1 * d2
                total = mul + res[i+j+1]

                res[i+j+1] = total % 10
                res[i+j] += total // 10


        return ''.join(map(str,res)).lstrip("0")
        