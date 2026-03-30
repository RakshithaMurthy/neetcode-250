class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed) and sort by position
        cars = sorted(zip(position, speed))
        
        stack = []  # This will store the times to reach the target
        fleets = 0
        
        # Iterate over the cars in reverse order (from the furthest to the closest to the target)
        for pos, spd in reversed(cars):
            # Calculate the time it takes for the current car to reach the target
            time = (target - pos) / spd
            
            # If the stack is empty or the current car's time is greater than the last car's time,
            # it forms a new fleet
            if not stack or time > stack[-1]:
                fleets += 1
                stack.append(time)  # Push the current car's time onto the stack
        
        return fleets