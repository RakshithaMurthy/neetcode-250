import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count, char))
        
        res = []
        
        while heap:
            count1, char1 = heapq.heappop(heap)
            
            # check last two characters
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break  # cannot add any more
                count2, char2 = heapq.heappop(heap)
                res.append(char2)
                count2 += 1  # remember counts are negative
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count1, char1))
            else:
                res.append(char1)
                count1 += 1
                if count1 != 0:
                    heapq.heappush(heap, (count1, char1))
        
        return ''.join(res)
