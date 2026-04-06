from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        path = []
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            prereq = q.popleft()
            path.append(prereq)
            for course in adj[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        if len(path) == numCourses:
            return path
        else:
            return []
            