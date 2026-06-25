class Solution:
    def trap(self, height: List[int]) -> int:

        if(len(height) == 0):
            return 0

        a = 0
        b = len(height) - 1

        a_mh = 0
        b_mh = 0

        res = 0
        
        a_mh = height[a]
        b_mh = height[b]
        while a < b:

            print(str(a) + " : " + str(b))
            print(str(height[a]) + " h " + str(height[b]))
            


            if(a_mh <= b_mh):
                print("left")
                
                if(min(a_mh, b_mh) - height[a] > 0):
                    res += min(a_mh, b_mh) - height[a]
                    print("+" + str(min(a_mh, b_mh) - height[a]))
                a += 1

                if(a_mh < height[a]):
                    a_mh = height[a]

                
            else:
                print("right")
                
                if(min(a_mh, b_mh) - height[b] > 0):
                    res += min(a_mh, b_mh) - height[b]
                    print("+" + str(min(a_mh, b_mh) - height[b]))
                b -= 1

                if(b_mh < height[b]):
                    b_mh = height[b]
            print(str(a_mh) + " - " + str(b_mh) + "\n")
                
                

            

        return res
                

        