class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        number = 0

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Read optional sign
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # Read digits
        while i < n and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        number *= sign

        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number