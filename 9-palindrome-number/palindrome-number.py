class Solution:
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 are not palindromes,
        # except 0 itself.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits: middle digit can be ignored
        return x == reversed_half or x == reversed_half // 10