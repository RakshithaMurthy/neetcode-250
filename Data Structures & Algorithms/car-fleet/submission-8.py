class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack =[]
        fleets = 0

        for pos,spd in cars:
            time = (target - pos)/spd
            if not stack or time > stack[-1]:
                fleets +=1
                stack.append(time)

        return fleets
        