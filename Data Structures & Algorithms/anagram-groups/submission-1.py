class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HM = {}
        out = []
        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in HM:
                HM[sort_s].append(s)
            else:
                HM[sort_s] = [s]

        for key in list(HM):
            out.append(HM[key])
        
        return out
