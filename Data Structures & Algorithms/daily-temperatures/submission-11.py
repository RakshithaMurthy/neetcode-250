class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack =[]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, temp = stack.pop()
                result[idx] = i - idx
            stack.append((i,t))

        return result


'''
#Temperatures II - Circular version
def dailyTemperaturesII(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []  # stores indices

    # Traverse twice for circular effect
    for i in range(2 * n):
        while stack and temperatures[i % n] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = (i - idx) % n
        if i < n:
            stack.append(i)

    return res

Second warmer day

def secondWarmerDay(temperatures):
    n = len(temperatures)
    res = [0] * n
    
    stack1 = []  # waiting for first warmer
    stack2 = []  # waiting for second warmer
    
    for i, temp in enumerate(temperatures):
        
        # Step 1: resolve second warmer
        while stack2 and temp > temperatures[stack2[-1]]:
            idx = stack2.pop()
            res[idx] = i - idx
        
        # Step 2: move from stack1 to stack2
        temp_stack = []
        while stack1 and temp > temperatures[stack1[-1]]:
            temp_stack.append(stack1.pop())
        
        while temp_stack:
            stack2.append(temp_stack.pop())
        
        # Step 3: push current index
        stack1.append(i)
    
    return res


#kth warmer day
def kthWarmerDay(temperatures, k):
    n = len(temperatures)
    res = [0] * n
    
    stacks = [[] for _ in range(k)]  # k stacks
    
    for i, temp in enumerate(temperatures):
        
        # Traverse stacks from last to first
        for level in range(k - 1, -1, -1):
            while stacks[level] and temp > temperatures[stacks[level][-1]]:
                idx = stacks[level].pop()
                
                if level == k - 1:
                    res[idx] = i - idx  # k-th warmer found
                else:
                    stacks[level + 1].append(idx)
        
        # Add current index to first stack
        stacks[0].append(i)
    
    return res

'''

        