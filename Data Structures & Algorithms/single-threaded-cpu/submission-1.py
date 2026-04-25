class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [(et,pt,i) for i, (et,pt) in enumerate(tasks)]
        tasks.sort()

        result=[]
        heap =[]
        time = 0
        i =0
        n = len(tasks)

        while i<n or heap:
            # if no task available, jump time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # add all available tasks
            while i<n and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(heap, (pt, idx))
                i+=1

            # process next task
            pt, idx = heapq.heappop(heap)
            time +=pt
            result.append(idx)

        return result


        