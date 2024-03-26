class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print("sorted list:", nums1)
        len_SortedArray = len(nums1)

        # odd - [1,2,3,4,5]
        # even - [1,2,3,4,5,6] = 3,4 -> 3.5

        if len_SortedArray % 2 == 0:  # even
            median_idx1 = (len_SortedArray // 2) - 1
            median_idx2 = median_idx1 + 1
            avg_median = (nums1[median_idx1] + nums1[median_idx2]) / 2
            return avg_median
        else:
            median_idx = int(len_SortedArray / 2)
            return nums1[median_idx]


ar1 = [11, 9, 15,13]
ar2 = [2, 10, 6]
#findMedianSortedArrays(ar1, ar2)

nums1 = [1,3]
nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
