class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ')' : '(', '}' : '{', ']' : '['}
        stack =[]
        for i in s:
            if i in bracket_map.values():  # If it's an opening bracket
                stack.append(i)
            elif i in bracket_map.keys():  # If it's a closing bracket
                if not stack or stack[-1] != bracket_map[i]:  # Mismatch or empty stack
                    return False
                stack.pop()  # Valid match, remove the opening bracket
        return not stack  # Return True if all brackets matched
