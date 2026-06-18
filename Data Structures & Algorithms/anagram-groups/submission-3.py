class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)

        for s in strs:
            counter = [0] * 26

            for i in s:
                counter[ord(i) - ord('a')] += 1

            anagram_dict[tuple(counter)].append(s)
        
        return list(anagram_dict.values())