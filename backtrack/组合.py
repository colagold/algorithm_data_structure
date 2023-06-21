class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        select=[]
        nums=[i+1 for i in range(n)]
        def backtrack(nums,start):
            if len(select)==k:
                res.append(select[:])
                return
            for i in range(start,n):
                select.append(nums[i])
                backtrack(nums,i+1)
                select.pop()
        backtrack(nums,0)
        return res