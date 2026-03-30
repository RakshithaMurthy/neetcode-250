import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # attach index
        tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        tasks.sort()

        res = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            # if no available task → jump time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # push all available tasks
            while i < n and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1

            # process next task
            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)

        return res

        