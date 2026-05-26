class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        n = len(strs)
        str1 = []

        for i in range(n):
            
            l = len(strs[i])
            dic1 = {}
            curr_res = []

            if strs[i] in str1:
                continue

            for x in range(l):
                dic1[strs[i][x]] = dic1.get(strs[i][x],0) + 1

            for j in range(i,n):

                lj = len(strs[j])
                dicj = {}

                for y in range(lj):
                    dicj[strs[j][y]] = dicj.get(strs[j][y],0) + 1

                if dic1 == dicj:
                    curr_res.append(strs[j])
                    str1.append(strs[j])

            res.append(curr_res)
            str1.append(strs[i])

        return res

        