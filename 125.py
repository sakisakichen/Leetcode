class Solution:
    def isPalindrome(self, s: str) -> bool:
        # temp = ""
        # for c in s:
        #     if c.isalnum():
        #         temp += c.lower()
        # print(temp)

        # return temp == temp[::-1]
        # join() 是用來合併可迭代對象（如 list） 

        # 方法二 雙指針 时间复杂度：O(n) 空间复杂度：O(1)
        L = 0 
        R = len(s) - 1
        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False 
            
            L += 1
            R -= 1
        return True
            