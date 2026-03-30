from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        # store all prerequisites for each course
        prereq = [set() for _ in range(numCourses)]

        # topological sort
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()

            for v in graph[u]:
                # propagate
                prereq[v].update(prereq[u])
                prereq[v].add(u)

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # answer queries
        return [u in prereq[v] for u, v in queries]