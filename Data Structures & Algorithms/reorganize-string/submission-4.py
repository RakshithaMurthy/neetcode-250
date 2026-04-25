class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        heap = [[-count,char] for char, count in freq.items()]
        heapq.heapify(heap)

        prev = None
        res=[]

        while heap or prev:
            if prev and not heap:
                return ""

            c, ch = heapq.heappop(heap)
            res.append(ch)
            c += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if c!=0:
                prev = [c, ch]

        return "".join(res)



        