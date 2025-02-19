from collections import defaultdict 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # 建一個計數器 來計算出現幾次  
    # 時間複雜度 O(M+N) 空間複雜度 O(1)
        # counter = {}
        # for c in magazine:
        #     if c in counter:
        #         counter[c] += 1 
        #     else:
        #         counter[c] = 1   
        counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1

        for c in ransomNote:
            if c not in counter or counter[c]<= 0:
                return False 

            else:
                counter[c] -= 1
        return True 

solution = Solution()
result = solution.canConstruct("aa", "aab")
print(result)