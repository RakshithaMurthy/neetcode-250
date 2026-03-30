class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed) and sort by position
        cars = sorted(zip(position, speed))
        
        fleets = 0
        time_to_reach = 0
        
        # Iterate over the cars in reverse order (from the furthest to the closest to the target)
        for pos, spd in reversed(cars):
            # Calculate the time it takes for the current car to reach the target
            time = (target - pos) / spd
            
            # If the current car takes longer than the last car's time to reach the target,
            # it forms a new fleet
            if time > time_to_reach:
                fleets += 1
                time_to_reach = time  # Update the time to the current car's time
        
        return fleets