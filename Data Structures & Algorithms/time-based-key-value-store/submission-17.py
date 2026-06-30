class TimeMap:

    def __init__(self):
        self.names = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.names[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        name_vals = self.names[key]

        l = 0
        r = len(name_vals) - 1

        res = ""
        print(name_vals)
        while l <= r:
            m = l + (r - l) // 2

            if timestamp < name_vals[m][0]:   
                r = m - 1
            else:
                res = name_vals[m][1]
                l = m + 1

        return res
