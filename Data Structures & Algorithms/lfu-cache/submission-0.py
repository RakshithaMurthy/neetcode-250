from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyMap = {}  # key -> (value, freq)
        self.freqMap = defaultdict(OrderedDict)  # freq -> keys
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        value, freq = self.keyMap[key]

        # remove from current freq
        del self.freqMap[freq][key]

        # if this was the only key with minFreq → update
        if not self.freqMap[freq]:
            del self.freqMap[freq]
            if self.minFreq == freq:
                self.minFreq += 1

        # add to next freq
        self.freqMap[freq + 1][key] = None
        self.keyMap[key] = (value, freq + 1)

        return value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyMap:
            # update value and bump freq
            self.keyMap[key] = (value, self.keyMap[key][1])
            self.get(key)
            return

        # eviction
        if len(self.keyMap) >= self.cap:
            # remove LRU from minFreq
            k, _ = self.freqMap[self.minFreq].popitem(last=False)
            del self.keyMap[k]

            if not self.freqMap[self.minFreq]:
                del self.freqMap[self.minFreq]

        # insert new key
        self.keyMap[key] = (value, 1)
        self.freqMap[1][key] = None
        self.minFreq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)