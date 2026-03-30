class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(current_str : str,open_count:int, close_count:int):

            if open_count == n and close_count ==n:
                result.append(current_str)
                return 

            if open_count<n:
                backtrack(current_str + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current_str + ')', open_count, close_count + 1)
        
        result =[]
        backtrack('', 0, 0)
        return result
        