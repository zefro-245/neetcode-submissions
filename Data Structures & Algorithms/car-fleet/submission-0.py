class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed), reverse=True)
        # stack.append((target-cars[0][0])/cars[0][1])
        for pos, speed in cars:
            time = (target-pos)/speed
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)