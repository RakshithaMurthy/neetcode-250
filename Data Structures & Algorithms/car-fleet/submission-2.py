class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        
        time_to_reach = 0
        fleet = 0
        for pos,spd in cars:   
            time = (target - pos)/spd

            if time > time_to_reach:
                fleet +=1
                time_to_reach = time
        return fleet
        