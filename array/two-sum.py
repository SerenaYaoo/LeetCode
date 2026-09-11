class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            current_number = nums[i]
            wanted = target - current_number
            if wanted in seen:
                return [i, seen[wanted]]
            seen[current_number] = i
        return []

                
