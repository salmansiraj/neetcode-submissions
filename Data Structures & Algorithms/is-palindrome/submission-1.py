class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        stripped_vals = [s[i].lower() for i in range(len(s)) if s[i].isalnum()]


        return stripped_vals == stripped_vals[::-1]