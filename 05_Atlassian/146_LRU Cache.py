class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.cap:
                del self.cache[next(iter(self.cache))]
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)