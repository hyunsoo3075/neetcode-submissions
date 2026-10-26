class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        for i in range(len(nums)):
            if (nums[i] in storage):
                return True
            else:
                storage.add(nums[i])
        return False