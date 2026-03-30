class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Manual frequency count (A–Z)
        freq = [0] * 26
    
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
    
        max_freq = max(freq)
    
        # Count how many tasks have max frequency
        max_count = 0
        for f in freq:
            if f == max_freq:
                max_count += 1
    
        # Apply greedy formula
        intervals = (max_freq - 1) * (n + 1) + max_count
    
        return max(len(tasks), intervals)
