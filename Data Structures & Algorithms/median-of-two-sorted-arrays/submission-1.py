class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        half = size // 2

        A = nums1
        B = nums2

        if len(A) > len(B):
            A = nums2
            B = nums1
        
        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float('-inf')
            rightA = A[i+1] if i + 1 < len(A) else float('inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightB = B[j+1] if j + 1 < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if size % 2 == 0:
                    return (max(leftA,leftB) + min(rightA, rightB)) / 2
                return min(rightA, rightB)

            if leftA > rightB:
                r = i - 1
            else:
                l = i + 1