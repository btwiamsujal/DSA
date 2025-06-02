class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 0:
            k = l // 2
            median = (nums1[k] + nums1[k-1]) / 2.0
            return round(median, 5)
        else:
            k = l // 2
            median = nums1[k]
            return round(median, 5)


