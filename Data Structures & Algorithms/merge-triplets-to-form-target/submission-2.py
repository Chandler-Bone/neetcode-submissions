class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        trip_len = len(triplets)
        curr_trip = 0
        target_found = False

        while curr_trip < 3:

            i = 0
            while i < trip_len:

                if triplets[i][curr_trip] > target[curr_trip]:
                    del triplets[i]
                    trip_len -= 1

                i += 1

            curr_trip += 1

        # print(triplets)
        curr_trip = 0
        while curr_trip < 3:

            i = 0
            target_found = False
            while i < trip_len:

                if triplets[i][curr_trip] == target[curr_trip]:
                    target_found = True

                i += 1

            if target_found == False:
                return False

            curr_trip += 1

        
        return True