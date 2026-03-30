from typing import List
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # Step 1: Build graph
        graph = defaultdict(set)
        
        # Initialize all unique characters
        for word in words:
            for char in word:
                graph[char]
        
        # Build edges
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            min_len = min(len(w1), len(w2))
            
            # Edge case: prefix invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        # Step 2: Topological sort (DFS)
        visited = {}  # char → state
        result = []
        
        def dfs(char):
            if char in visited:
                return visited[char] == 2
            
            visited[char] = 1  # visiting
            
            for neighbor in graph[char]:
                if visited.get(neighbor, 0) == 1:
                    return False  # cycle
                if not dfs(neighbor):
                    return False
            
            visited[char] = 2  # visited
            result.append(char)
            return True
        
        for char in graph:
            if char not in visited:
                if not dfs(char):
                    return ""
        
        result.reverse()
        return "".join(result)

        