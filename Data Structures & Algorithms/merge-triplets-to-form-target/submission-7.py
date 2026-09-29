class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        i = 0
        trip_len = len(triplets)

        while i < 3:

            j = 0
            while j < trip_len:
                if triplets[j][i] > target[i]:
                    del triplets[j]
                    trip_len -= 1
                    continue

                j += 1
            
            i += 1

        # print(triplets)        
        trip_match = False
        i = 0
        while i < 3:
            trip_match = False
            j = 0
            while j < len(triplets):
                if triplets[j][i] == target[i]:
                    trip_match = True
                j += 1

            if trip_match == False:
                return False
            i += 1

        return True
