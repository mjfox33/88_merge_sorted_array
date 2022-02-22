class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
            return
        pointer = n+m-1
        while pointer >=0 and n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[pointer] = nums2[n-1]
                n -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums1[m-1]
                m -= 1
                pointer -= 1
                
        while n > 0 and pointer >= 0:
            nums1[pointer] = nums2[n-1]
            n -= 1
            pointer -= 1
            
        while m > 0 and pointer >= 0:
            nums1[pointer] = nums1[m-1]
            m -= 1
            pointer -= 1