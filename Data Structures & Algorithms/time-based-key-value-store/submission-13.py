class TimeMap:

    def __init__(self):
        self.key_vals = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_vals[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        t_list = self.key_vals[key]

        if not t_list:
            return ""

        times = [i[0] for i in t_list]

        l = 0
        r = len(times) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if times[m] <= timestamp:
                res = t_list[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        
