class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)) == 0:
            return [[]]
        sorted_dict:[str,[str]] = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in sorted_dict:
                sorted_dict[sorted_str].append(strs[i])
            else:
                sorted_dict[sorted_str] = [strs[i]]
        return list(sorted_dict.values())