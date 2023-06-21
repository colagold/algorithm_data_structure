class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        track=[]
        def backtrack(nums,start):
            res.append(track[:])
            for i in range(start,len(nums)):
                track.append(nums[i])
                backtrack(nums,i+1)
                track.pop()
        backtrack(nums,0)
        return res

if __name__ == "__main__":
    print(Solution().subsets([1,2,3]))