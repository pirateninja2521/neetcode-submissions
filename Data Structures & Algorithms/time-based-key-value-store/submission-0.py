class TimeMap:

    def __init__(self):
        self.keyList = defaultdict(list)
               
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyList[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        keyList = self.keyList[key]

        ans = ""
        
        l, r = 0, len(keyList) - 1

        while l <= r:
            mid = (l + r) // 2
            midTimestamp, minValue = keyList[mid]

            if midTimestamp <= timestamp:
                ans = minValue
                l = mid + 1
            else:
                r = mid - 1

        return ans