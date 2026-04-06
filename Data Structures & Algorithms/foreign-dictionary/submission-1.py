from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}
        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]
            shortest = min(len(prev), len(curr))
            if len(prev) > len(curr) and prev[:shortest] == curr[:shortest]:
                return ""
            for j in range(shortest):
                if prev[j] != curr[j]:
                    if curr[j] not in adj[prev[j]]:
                        adj[prev[j]].add(curr[j])
                        indegree[curr[j]] += 1
                    break
        
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        path = []
        while q:
            c = q.popleft()
            path.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        print(path)
        
        if set(path) == set("".join(words)):
            return "".join(path)
        else:
            return ""
