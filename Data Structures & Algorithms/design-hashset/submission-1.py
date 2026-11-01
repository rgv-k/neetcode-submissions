class MyHashSet:

    def __init__(self):
        self.hs = {}

    def add(self, key: int) -> None:
        if key in self.hs:
            return
        
        self.hs[key] = True

    def remove(self, key: int) -> None:
        if key in self.hs:
            del self.hs[key]

    def contains(self, key: int) -> bool:
        return self.hs.get(key, False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)