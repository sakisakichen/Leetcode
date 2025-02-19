from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # brutal way
        # curr_sum = -1 
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] + nums[j] < k and nums[i] + nums[j] > curr_sum:
        #             curr_sum = nums[i] + nums[j]      
        # return curr_sum

        # 雙指針 
        nums.sort()
        L,R = 0 , len(nums) - 1
        curr_sum = -1 
        while L < R:
            total = nums[L] + nums[R]
            if total < k:
                curr_sum = max(total, curr_sum)
                L += 1

            else:
                R -= 1  
        if curr_sum != -1:
            return curr_sum
        else:
            return -1 

solution = Solution()

result = solution.twoSumLessThanK([34,23,1,24,75,33,54,8],60)
print(result)