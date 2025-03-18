class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # num~num 之中
        # low < nums[0] : missing at the start 
        # high > nums[-1] : missing at the end 

        ans = []
        n = len(nums)

        if n == 0 :
            return [[lower,upper]]
        
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])


        for i in range(n -1):
            # if 2 numbers diff = 1
            if nums[i + 1] -nums[i] <= 1:
                continue
            ans.append([nums[i] +1 , nums[i+1] -1 ]) 
        

        if upper > nums[-1]:
            ans.append([nums[-1] + 1 ,upper])
        return ans 
