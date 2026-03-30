from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        visited = set(["0000"])

        while q:
            node, steps = q.popleft()

            if node == target:
                return steps

            for i in range(4):
                digit = int(node[i])

                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_state = node[:i] + str(new_digit) + node[i+1:]

                    if new_state not in dead and new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, steps + 1))

        return -1

        