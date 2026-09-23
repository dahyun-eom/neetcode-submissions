class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        return_list = []
        i=0
        for str in strs:
            origin = str
            str = ''.join(sorted(str))
            if str not in my_dict:
                my_dict[str] = i
                return_list.append([origin])
                i = i+1
            else:
                return_list[my_dict[str]].append(origin)
        return return_list
