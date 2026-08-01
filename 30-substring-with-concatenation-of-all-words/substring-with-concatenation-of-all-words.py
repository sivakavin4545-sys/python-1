from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        need = Counter(words)
        size, count = len(words[0]), len(words)
        result = []

        for start in range(size):
            left = start
            seen = Counter()
            used = 0

            for right in range(start, len(s) - size + 1, size):
                word = s[right:right + size]

                if word not in need:
                    seen.clear()
                    used = 0
                    left = right + size
                    continue

                seen[word] += 1
                used += 1

                while seen[word] > need[word]:
                    seen[s[left:left + size]] -= 1
                    used -= 1
                    left += size

                if used == count:
                    result.append(left)

        return result