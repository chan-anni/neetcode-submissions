class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()
        c_list = list(clean)
        rev = c_list[::-1]
        return c_list == rev