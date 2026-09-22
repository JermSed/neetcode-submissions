class TimeMap:
    def __init__(self):
        self.dataStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dataStore:
            self.dataStore[key].append((value,timestamp))
        else:
            self.dataStore[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.dataStore:
            return ""
        arr = self.dataStore[key]
        left = 0
        right = len(arr) - 1

        while right >= left:

            mid = (right + left) // 2

            if arr[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        res = f'{arr[right][0]}'

        if right == -1:
            return ""
        if arr[right][1] > timestamp:
            return ""

        return res
