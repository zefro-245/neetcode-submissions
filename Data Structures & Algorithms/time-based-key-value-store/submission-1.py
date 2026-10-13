class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [(value, timestamp)]
        else:
            self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        content = self.data[key]
        left = 0
        right = len(content) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if content[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:        
            return content[right][0]
        return ""

