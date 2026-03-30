class TimeMap:

    def __init__(self):
        self. keystore = {} # Each key maps to a list of lists
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res =""
        values = self.keystore.get(key,[])
        l, r = 0, len(values) - 1
        while l <=r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m -1
        
        return res
        
#Time & Space Complexity

    #Time complexity: O(1)O(1) for set()set() and O(log⁡n)O(logn) for get()get().
    #Space complexity: O(m∗n)O(m∗n)

    #Where nn is the total number of values associated with a key and mm is the total number of keys. 