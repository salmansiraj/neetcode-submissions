class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        stripped_vals = [s[i].lower() for i in range(len(s)) if s[i].isalnum()]

        start, end = 0, len(stripped_vals) - 1

        while start <= end:
            if stripped_vals[start] != stripped_vals[end]:
                return False
            start += 1
            end -= 1
        
        return True