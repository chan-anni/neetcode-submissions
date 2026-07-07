class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        running = 1
        zeros = 0
        for num in nums:
            if (num!=0):
                running *= num
            else:
                zeros +=1
        if (zeros > 1): return [0]* len(nums)

        if (zeros == 1):
            for i, c in enumerate(nums):
                if c == 0: res.append(running)
                else: res.append(0)

            return res
        else: 
            for i in nums:
                res.append(int(running/i))
            return res
            
        