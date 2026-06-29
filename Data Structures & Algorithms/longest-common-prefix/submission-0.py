class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommon = ""
        index = 0
        for i in range(len(min(strs, key=len))):
            saved = strs[0][i] 
            for string in strs:
                if string[i] != saved: return longestCommon
            longestCommon += saved
        return longestCommon