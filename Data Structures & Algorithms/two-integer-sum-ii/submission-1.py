class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            if numbers[r] + numbers[l] == target:
                res = [l+1, r+1]
                return res
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                r -= 1