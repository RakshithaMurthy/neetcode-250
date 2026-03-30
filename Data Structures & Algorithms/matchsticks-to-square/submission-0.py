class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return all(side == target for side in sides)

            for j in range(4):
                if sides[j] + matchsticks[i] > target:
                    continue

                # choose
                sides[j] += matchsticks[i]

                if backtrack(i + 1):
                    return True

                # backtrack
                sides[j] -= matchsticks[i]

                # 🔥 pruning
                if sides[j] == 0:
                    break

            return False

        return backtrack(0)

        