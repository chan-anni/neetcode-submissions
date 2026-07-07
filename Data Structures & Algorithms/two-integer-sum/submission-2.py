class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in HM:
                return [HM[val],i]
            HM[nums[i]] = i
