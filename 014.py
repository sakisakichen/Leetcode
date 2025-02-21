from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if str== '':
        #     return ""
        # # find the min length 
        # min_length = float('inf')

        # for s in strs:
        #     if len(s) < min_length:
        #         min_length = len(s)
        
        # i = 0 
        # while i < min_length:
        #     for s in strs:
        #         if s[i] != strs[0][i]:
        #             return s[:i]
        #     i += 1  
        
        # return s[:i]

    # """
    # 首先，如果陣列為空或其中一個字串為空，直接返回空字串 ""。
    # 然後，我們可以將第一個字串設為參考前綴，然後與陣列中的其他字串逐一比較。
    # 每當發現某個字串的前綴不符合當前前綴時，則縮短當前前綴直到符合為止。
    # """
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

solution = Solution()
test = solution.longestCommonPrefix(["flower","flow","flight"])
print(test)