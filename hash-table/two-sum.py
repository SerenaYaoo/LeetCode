class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        result = []

        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [i, seen[compliment]]
            
            seen[num] = i
        return result