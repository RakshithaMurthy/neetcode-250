class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ')' : '(', '}' : '{', ']' : '['}
        stack =[]
        for i in s:
            if i in bracket_map.values():
                stack.append(i)
            elif i in bracket_map.keys():
                if not stack or stack[-1] != bracket_map[i]:
                    return False
                stack.pop()
        return not stack
             