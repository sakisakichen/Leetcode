from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brutal way  : T O(n^2) S O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return [] # 如果沒有解，避免出錯
       
       
        # Hash Map     
       ans = {}
       for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in ans:
            ans[nums[i]] = i 
        else:
            return [ans[diff],i]

solution = Solution()
result = solution.twoSum([2,7,11,15],9)


print(result)