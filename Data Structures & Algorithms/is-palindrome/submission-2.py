class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        string = string.lower()
        pt1 = 0
        pt2 = len(string) - 1
        while pt1 <= pt2:
            if string[pt1] != string[pt2]: return False
            pt1+= 1
            pt2-=1
        return True