class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []  
        self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, potentials = "", self.timeMap.get(key,[])
        
        l,r = 0, len(potentials) -1

        while l<=r:
            m = (l+r) //2
            if potentials[m][1] <= timestamp:
                res = potentials[m][0]
                l = m+1
            else:
                r = m-1

        return res