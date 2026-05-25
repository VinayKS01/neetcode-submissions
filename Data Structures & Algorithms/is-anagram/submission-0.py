class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ds = {}
        dt = {}

        for i in s:
            ds[i] = ds.get(i,0) + 1

        for i in t:
            dt[i] = dt.get(i,0) + 1

        if ds == dt:
            return True
        else:
            return False
        