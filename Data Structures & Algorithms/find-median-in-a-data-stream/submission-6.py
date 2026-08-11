class MedianFinder:

    def __init__(self):
        self.max_heap = [] #left side
        self.min_heap = [] #right side


    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return

        # if num bigger than right side, put it there, else other
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)

        # balance them if more than length diff of 2
        if abs(len(self.max_heap) - len(self.min_heap)) == 2:
            if len(self.max_heap) > len(self.min_heap):
                swap_val = heapq.heappop_max(self.max_heap)
                heapq.heappush(self.min_heap, swap_val)
            else:
                swap_val = heapq.heappop(self.min_heap)
                heapq.heappush_max(self.max_heap, swap_val)
        
        # print(str(self.max_heap) + " - " + str(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0])
        else:
            return float(self.min_heap[0])
        