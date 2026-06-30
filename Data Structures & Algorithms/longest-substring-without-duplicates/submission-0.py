class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxLen = 0
        left = 0
        right = 0
        while(right < len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            if freq[s[right]] > 1:
                while freq[s[right]] > 1:
                    freq[s[left]] -= 1
                    left += 1
                    if right - left + 1 > maxLen: maxLen = right - left + 1
            if right - left + 1 > maxLen: maxLen = right - left + 1
            right += 1
        return maxLen
