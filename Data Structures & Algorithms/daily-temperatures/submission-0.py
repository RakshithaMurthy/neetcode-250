class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with zeros
        stack = []  # This will store indices of the temperatures

        for i in range(n):
            # While there are indices in the stack and the current temperature is greater
            # than the temperature at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()  # Get the index of the cooler temperature
                result[index] = i - index  # Calculate the number of days until a warmer temperature
            
            # Push the current index onto the stack
            stack.append(i)

        return result