class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"]" : "[", ")" : "(", "}" : "{"}
        stack =[]

        for ch in s:
            if ch in brackets:
                if not stack or stack[-1] != brackets[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack




   
        