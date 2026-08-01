class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            if i == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[i - 1]

            if i == m:
                right1 = float('inf')
            else:
                right1 = nums1[i]

            if j == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[j - 1]

            if j == n:
                right2 = float('inf')
            else:
                right2 = nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1