class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_map = dict()

        for s in strs:
            sorted_s = str(sorted(s))
            if (sorted_s in str_map):
                str_map[sorted_s] = str_map.get(sorted_s) + [s]
            else:
                str_map[sorted_s] = [s]
        
        return list(str_map.values())