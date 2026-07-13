class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try again
        # create a list from 1 banana to max bananas:
        n = max(piles)
        # speed = [i for i in range(n)] # Removed to save memory, not strictly necessary for fix
        
        l, r = 1, n
        res = r

        while l <= r:
            curr = (l+r)//2 # chosen number of bananas speed to test
            if curr == 0: 
                l = 1
                continue
            time = 0
            for p in piles:
                time += math.ceil(float(p) / curr)
            if time <= h:

                res = curr
                r = curr - 1
            else:
                l = curr + 1
        return res