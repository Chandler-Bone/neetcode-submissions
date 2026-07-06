class TimeMap:

    def __init__(self):
        self.people = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val_times = self.people[key]

        l = 0
        r = len(val_times) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2

            m_val = val_times[m][0]
            m_timestamp = val_times[m][1]
            

            if m_timestamp == timestamp:
                return m_val

            if m_timestamp <= timestamp:
                res = val_times[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
