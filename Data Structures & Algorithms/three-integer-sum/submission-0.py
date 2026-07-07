class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            mapping = {}
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in mapping:
                    result.add((nums[i], diff, nums[j]))
                mapping[nums[j]] = j
        
        return [list(t) for t in result]