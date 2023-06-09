
class Solution(object):
    def permute(self,nums):
        res=[]
        def backtrack(candidates,select):
            if len(candidates)==len(select):
                res.append(select[:])
                return
            for candidate in candidates:
                if candidate in select:
                    continue
                select.append(candidate)
                backtrack(candidates,select)
                select.pop()
        select=[]
        backtrack(nums,select)
        return res

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))