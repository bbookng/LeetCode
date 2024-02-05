class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        array.sort()
        n = len(array)

        if n % 2:
            return array[n // 2]
        else:
            return (array[n // 2] + array[n // 2 - 1]) / 2

