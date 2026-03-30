class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]  # (current string, open count, close count)

        while stack:
            current, open_count, close_count = stack.pop()

            # If we have used n opening and n closing parentheses, add to result
            if open_count == n and close_count == n:
                result.append(current)
                continue

            # If we can add an opening parenthesis
            if open_count < n:
                stack.append((current + '(', open_count + 1, close_count))

            # If we can add a closing parenthesis
            if close_count < open_count:
                stack.append((current + ')', open_count, close_count + 1))

        return result