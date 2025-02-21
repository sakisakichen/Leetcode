class Solution:
    def romanToInt(self, s: str) -> int:
        dict_s = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    #   hashmap 
        # ans = 0 
        # prev_value = 0 

        # for char in reversed(s):
        #     curr_value = dict_s[char]
        #     if curr_value < prev_value:
        #         ans -= curr_value 
        #     else:
        #         ans += curr_value 
        #     prev_value = curr_value 
        # return ans 
        
    # iterate 
        total = 0 
        
        for i in range(len(s)):
            if i < len(s)-1 and dict_s[s[i]] < dict_s[s[i+1]]:
                total -= dict_s[s[i]]
            else:
                total += dict_s[s[i]]
        
        
        return total 

solution = Solution()
test = solution.romanToInt("XL")
print(test)
