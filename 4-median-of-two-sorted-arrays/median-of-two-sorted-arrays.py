class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            max_left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            min_right1 = float("inf") if cut1 == m else nums1[cut1]

            max_left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            min_right2 = float("inf") if cut2 == n else nums2[cut2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))

                return (max(max_left1, max_left2) +
                        min(min_right1, min_right2)) / 2.0

            if max_left1 > min_right2:
                high = cut1 - 1
            else:
                low = cut1 + 1