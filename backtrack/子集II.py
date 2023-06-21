class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        select=[]
        def backtrack(nums,start):
            res.append(select[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]: #剪枝
                    continue
                select.append(nums[i])
                backtrack(nums,i+1)
                select.pop()
        backtrack(nums,0)
        return res