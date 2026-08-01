class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs:
            while prefix and word[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix