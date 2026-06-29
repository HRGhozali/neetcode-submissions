class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        wordArrS = [0] * 26
        wordArrT = [0] * 26
        for letter in s:
            wordArrS[ord(letter)-97] += 1
        for letter in t:
            wordArrT[ord(letter)-97] += 1
        if wordArrS == wordArrT: return True
        return False