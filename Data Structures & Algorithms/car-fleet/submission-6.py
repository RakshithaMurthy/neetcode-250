
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, sort by position descending
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        fleets = 0
        prev_time = 0  # time taken by the last fleet
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev_time:
                fleets += 1  # new fleet
                prev_time = time  # update the last fleet time
            # else: joins previous fleet, do nothing
        
        return fleets
