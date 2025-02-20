# from collections import Counter 
from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return s.sort() == t.sort()
        # sort() 只能用在 list，而不能直接用在字串 (str) 上
        # 方法一 ：sorted() 會返回 排序後的新列表 T  O(N log N), S O(N)
        # return sorted(s) == sorted(t)
    
        # 方法二 ：counter 方式 T O(n), S O(1)
        # return Counter(s) == Counter(t)

        # 方法三 ：dict 方式 T O(n), S O(1)
        # if len(s) != len(t):
        #     return False

        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            dict_s[i] += 1

        for j in t:
            if j not in dict_t:
                dict_t[j] = 1
            dict_t[j] += 1 
    
        return dict_s == dict_t

solution = Solution()
print(solution.isAnagram("anagram","nagaram"))