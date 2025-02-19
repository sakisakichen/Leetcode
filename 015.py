from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()  # 先排序
        ans = []

        for i in range(len(nums) - 2):  # 至少要有三個元素
            if i > 0 and nums[i] == nums[i - 1]:  
                continue  # 跳過重複的元素，避免相同組合

            left = i + 1  
            right = len(nums) - 1  

            while left < right:  
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 確保不重複
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans





test_case = [-1,0,1,2,-1,-4]
solution = Solution()

result = solution.threeSum(test_case)

# print(f"input:{test_case}, output:{result}")

print(solution.threeSum(test_case))