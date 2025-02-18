class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2 pointers 
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        # return True if i == len(s) else False
            if i == len(s):
                return True
        return False