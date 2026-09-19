class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_count = defaultdict(int)
        hand_min_heap = []

        for i in hand:
            if i not in hand_count:
                heapq.heappush(hand_min_heap, i)
            hand_count[i] += 1

        while hand_min_heap:

            curr_strt = []
            for i in range(groupSize):
                curr_num = heapq.heappop(hand_min_heap)
                hand_count[curr_num] -= 1
                curr_strt.append(curr_num)

                if i != groupSize - 1 and (len(hand_min_heap) < 1 or hand_min_heap[0] != curr_num + 1):
                    return False

            for i in curr_strt:
                if hand_count[i] != 0:
                    heapq.heappush(hand_min_heap, i)
            
                
        
        # print(hand_min_heap)
        # print(hand_count)

        return True