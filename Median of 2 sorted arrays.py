class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        l = len(a)
        if len(a) % 2:
            return a[int((l-1)/2)]
        else:
            return (a[int(l/2)] +  a[int(l/2)-1])/2