class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            sorted_word = "".join(sorted(str))
            if sorted_word in dict:
                dict[sorted_word].append(str)
            else:
                dict[sorted_word] = [str]
        
        return list(dict.values())

        