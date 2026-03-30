class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    result = a + b
                elif i == "-":
                    result = a - b
                elif i == "*":
                    result = a * b
                elif i == "/":
                    result = int(a / b)
                stack.append(result)

            
        return stack[0]
        