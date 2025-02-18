from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
     
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k 


"""
if not required in place:
def removeElement(nums, val):
    return [num for num in nums if num != val]
時間複雜度為 O(n)

def removeElement(nums, val):
    new_nums = nums[:]  # 複製原列表，避免修改原數據
    while val in new_nums:
        new_nums.remove(val)  # 逐個刪除所有 val
    return new_nums
時間複雜度為 O(n²)，因為 remove() 每次刪除元素都要重新調整數組位置
"""
"""
        for i in range(len(nums)-1, -1, -1):  # 倒著遍歷，避免索引變化影響後續元素
            if nums[i] == val:
                nums.pop(i)  # pop() 是 remove() 的索引版本
        return len(nums)

        # 當 nums 很大時仍較慢 , O(n) O(n)
"""