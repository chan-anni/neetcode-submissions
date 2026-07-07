class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dist_nums = set(nums)
        if len(nums) > len(dist_nums):
            return True
        return False
        