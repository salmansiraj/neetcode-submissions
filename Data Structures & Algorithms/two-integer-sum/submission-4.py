class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = {}

        for index, number in enumerate(nums):
            res = target - number 

            if res in result:
                return [result[res], index]
            
            result[number] = index
        
        
