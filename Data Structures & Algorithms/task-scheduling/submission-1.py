class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: frequency count (no Counter)
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Step 2: build max heap (use negative values)
        max_heap = []
        for f in freq:
            if f > 0:
                heapq.heappush(max_heap, -f)

        time = 0
        cooldown = deque()  # (remaining_count, available_time)

        # Step 3: simulate CPU time
        while max_heap or cooldown:
            time += 1

            # Execute the most frequent available task
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # +1 because negative
                if count != 0:
                    cooldown.append((count, time + n))

            # Move tasks from cooldown back to heap if ready
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
