class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        res = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else: # nums[mid] > nums[hi]
                lo = mid + 1
            res = mid
        return nums[res]
