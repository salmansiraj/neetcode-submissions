class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, maxLength = 0, 0

        for r in range(len(s)):
            # cleanup dupe until we can continue
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, len(seen))
        
        return maxLength
            

