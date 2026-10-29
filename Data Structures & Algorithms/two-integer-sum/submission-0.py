class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_finder = {}
        for i in range(len(nums)):
            if(target - nums[i]) in sum_finder:
                return [sum_finder[target-nums[i]], i]
            sum_finder[nums[i]] = i
        return []