import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        for cnt, ch in [(a,'a'), (b,'b'), (c,'c')]:
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))

        res = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)

            # if last two are same as current → try second best
            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not heap:
                    break

                cnt2, ch2 = heapq.heappop(heap)

                res.append(ch2)
                cnt2 += 1  # reduce count

                if cnt2 != 0:
                    heapq.heappush(heap, (cnt2, ch2))

                heapq.heappush(heap, (cnt1, ch1))

            else:
                res.append(ch1)
                cnt1 += 1

                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, ch1))

        return "".join(res)