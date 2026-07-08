class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for i, v in enumerate(s):
            if v in dictS:
                dictS[v] += 1
            else:
                dictS[v] = 1
        
        dictT = {}
        for i, v in enumerate(t):
            if v in dictT:
                dictT[v] += 1
            else:
                dictT[v] = 1

        if len(dictS) != len(dictT): 
            return False

        for k, v in dictS.items():
            if k in dictT and v == dictT[k]:
                continue
            else:
                return False
        return True

            