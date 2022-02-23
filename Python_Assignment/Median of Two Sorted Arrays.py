# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
import statistics

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted(nums1)
        sorted(nums2)
        result=nums1
        for ch in nums2:
            if result.__contains__(ch):
                pass
            else:
                result.append(ch)
        sorted(result)
        print(float(statistics.median(result)))

sol=Solution()
nums1 = [1,2]
nums2 = [3,4]
sol.findMedianSortedArrays(nums1,nums2)


