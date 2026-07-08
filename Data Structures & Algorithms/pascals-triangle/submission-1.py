
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        i = 1
        res = [[1]]

        while i < numRows:
            row = [0] * (i + 1)
            row[0] = 1
            row[-1] = 1

            j = 1

            while j < i:
                row[j] = res[i - 1][j-1] + res[i-1][j]
                j += 1
            
            i += 1
            res.append(row)

        return res