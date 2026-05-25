class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        res = [0,0]

        for i in range(n):
            for j in range(i+1,n):

                if nums[i]+nums[j] == target:
                    res[0] = i
                    res[1] = j
                    return res


        return res      

        