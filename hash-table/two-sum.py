class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            current_char = nums[i]
            wanted = target - current_char
            for j in range(i+1, len(nums)):
                if nums[j] == wanted:
                    return [i, j]
        return []
            
                
