class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort(key=lambda x:x)
        # print(nums)
        seen = dict()
        for i in range(len(nums)-1):
            current = nums[i]
            for j in range(i, len(nums)):
                next_num = nums[j]
                needed = 0 - (current + next_num)
                if needed in seen and seen[needed] < i:
                    if [current, next_num, needed] not in result:
                        result.append([current, next_num, needed])
            seen[current] = i
        return result





        