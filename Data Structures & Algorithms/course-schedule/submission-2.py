class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0
        while q:
            course = q.popleft()
            count +=1

            for nei in graph[course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)

        return count == numCourses

        
        