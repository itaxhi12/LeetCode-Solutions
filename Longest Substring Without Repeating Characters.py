class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ''
        length = 0

        for char in s:
            if char not in sub_s:
                sub_s += char
            else:
                sub_s = sub_s[sub_s.index(char) + 1:] + char
            length = max(length, len(sub_s))
        return length