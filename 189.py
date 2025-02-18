class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法一 直接取最後一個數 新增到最前面
        # 總時間 O(3n) = O(n)，但如果 k 很大，會很慢！,空間複雜度：O(1)

        # for i in range(k):
        #     nums.insert(0,nums.pop())
        
        # 方法二 時間複雜度 O(n),空間複雜度是 O(n) ->nums[-k:] + nums[:-k] 會建立一個新的數組
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]

        # 方法三 反轉法的時間複雜度是 O(n)，空間 O(1)：
        # 先全部翻轉  在前半段翻轉一次  後半段在自己翻轉
        k = k % len(nums)
        l,r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r- 1

        l,r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r- 1

        l,r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r- 1