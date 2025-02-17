class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1 
        # brutal way：2 pointers  O(n*2)
        for i in range(len(haystack) - len(needle) + 1):
            # for j in range(len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i 
            if haystack[i: i + len(needle)] == needle:
                return i 
        return -1 

        for i in range(n - m + 1):  # 只需檢查到 (n - m) 位置
            if haystack[i:i + m] == needle:
                return i  # 返回第一次匹配的位置
        # 使用內建 find() 方法
        # return haystack.find(needle)