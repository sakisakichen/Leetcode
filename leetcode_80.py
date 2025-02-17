class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     j = 1 
    #     count = 1
    #     for i in range(1,len(nums)):
            
    #         if nums[i] == nums[i-1]:
    #             count += 1 
    #         else:
    #             count = 1

    #         if count <= 2:
    #             nums[j] = nums[i]
    #             j += 1
        
    #         print(nums) 
    #         print(count)
    #     return j 

        if len(nums) <= 2:  # 如果數組長度小於等於2，直接返回
            return len(nums)

        j = 2  # j 指向下一個可以放入新元素的位置
        for i in range(2, len(nums)):  # 從索引 2 開始遍歷
            if nums[i] != nums[j - 2]:  # 只要不是連續第三個重複元素，就保留
                nums[j] = nums[i]
                j += 1

        return j  # j 是新數組的長度