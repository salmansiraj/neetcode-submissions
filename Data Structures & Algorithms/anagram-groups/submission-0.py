class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i, v in enumerate(strs):
            counterSet = frozenset(Counter(v).items())
            if counterSet in result:
                result[counterSet].append(v)
            else:
                result[counterSet] = [v]
        
        return [val for key, val in result.items()]
        

