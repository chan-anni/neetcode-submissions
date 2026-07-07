class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        rev_nums = nums[::-1]
        print(rev_nums)
        for i in range(1, len(nums), 1):
            prefix.append(prefix[i-1]*nums[i-1])
            suffix.append(suffix[i-1]*rev_nums[i-1])

        rev_suffix = suffix[::-1]
        print(rev_suffix)
        
        return [prefix[i] * rev_suffix[i] for i in range(len(prefix))]

        

            
        