from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # Build pattern dictionary
        pattern_map = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear to prevent reprocessing
                pattern_map[pattern] = []
        
        return 0

        