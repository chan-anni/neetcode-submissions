class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # creating buckets for each count, with a max of len(nums) count something can be
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        print(count)

        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1): #going backwards from high -> low
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

        
        