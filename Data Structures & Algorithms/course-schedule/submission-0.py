from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        possible = 0
        while q:
            prereq = q.popleft()
            possible += 1
            for course in adj[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return possible == numCourses
