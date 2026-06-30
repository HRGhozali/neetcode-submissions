class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        string = string.lower()
        revStr = string[::-1]
        return string == revStr