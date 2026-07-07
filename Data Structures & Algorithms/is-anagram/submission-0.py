class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}

        for i in range(len(s)):
            if s[i] in result:
                result[s[i]] += 1
            else:
                result[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in result:
                if result[t[i]] == 1:
                    del result[t[i]]
                else:
                    result[t[i]] -= 1
            else:
                return False


        return True if len(result) == 0 else False