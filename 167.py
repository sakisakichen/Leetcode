class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # non-decreasing order 是遞增排列  可以用雙指針來找
        l , r = 0 , len(numbers)-1 

        while l < r :
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1 