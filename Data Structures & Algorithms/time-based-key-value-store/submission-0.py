class TimeMap:

    def __init__(self):
        self.history = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.history:
            self.history[key].append((timestamp, value))
        else:
            self.history[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.history: return ""

        l = 0
        r = len(self.history[key]) - 1
        best = -1
        values = self.history[key]

        while l <= r:
            mid = (l+r)//2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid  + 1
                best = mid
        

        return "" if best==-1 else self.history[key][best][1]


