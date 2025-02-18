class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 2 pointers
        z = m + n - 1
        x = m - 1
        y = n - 1 

        for i in range(z,-1,-1):
            if x < 0 :
                nums1[i] = num2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nume2[y]:
                nums1[i] = nums1[x]
                x-= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
