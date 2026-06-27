class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m_size = (len(matrix), len(matrix[0]))

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = l + (r - l) // 2
            m_val = matrix[m // m_size[1]][m % m_size[1]]

            if m_val > target:
                r = m - 1
            elif m_val < target:
                l = m + 1
            else:
                return True

        return False