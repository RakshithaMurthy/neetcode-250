class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if 1 in nums:
            return False

        parent = list(range(len(nums)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # map: prime → index
        prime_to_index = {}

        def get_primes(x):
            primes = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    primes.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                primes.add(x)
            return primes

        for i, num in enumerate(nums):
            primes = get_primes(num)

            for p in primes:
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                prime_to_index[p] = i

        root = find(0)
        return all(find(i) == root for i in range(len(nums)))