class Solution:
    def searchRange(self, nums, target):
        def find(first):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid

                if nums[mid] < target or (nums[mid] == target and not first):
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [find(True), find(False)]