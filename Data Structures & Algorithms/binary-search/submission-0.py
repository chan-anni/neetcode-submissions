class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            i = (low + high) // 2
            curr = nums[i]
            if curr > target:
                high = i - 1
            elif curr < target:
                low = i + 1
            elif curr == target:
                return i

        return -1