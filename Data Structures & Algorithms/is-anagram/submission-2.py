class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        if len(s) != len(t):
            return False
        for j in t:
            if j in s_dict and s_dict[j] >= 1:
                s_dict[j] -= 1
                continue
            else:
                return False
        return True
        