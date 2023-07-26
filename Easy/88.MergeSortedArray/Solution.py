class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        inPlaceIdx = -1
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[inPlaceIdx] = nums1[m - 1]
                m = m - 1
            else:
                nums1[inPlaceIdx] = nums2[n - 1]
                n = n - 1
            inPlaceIdx -= 1
        

            



