## 回溯
回溯是一种算法思想，可由递归实现。递归是一种解决问题的方法，而回溯是一种特定的算法实现。递归是通过调用自身来解决问题的一种策略，而回溯是在解空间中进行搜索并进行选择的算法。

**为什么要介绍定义？**
因为之前一直将递归当成回溯，这是个错误的思想。递归的范围会更大，其囊括了回溯。

## 回溯思想
解决回溯问题，实际上就是一个决策树的遍历过程，只需要思考如下三个问题：
1. 路径:就是已经做出的选择。
2. 选择列表：也就是当前可以做出的选择
3. 结束条件：要么满足要求，要么已经遍历结束。

**框架**
```text
result=[]
def backtrack(选择列表,路径):
    if 满足结束条件：
        result.add(路径)
        return
    for 选择 in 选择列表：
        做选择
        backtrack(选择列表，路径)
        撤销选择
```
在回溯算法中，撤销选择是为了回到上一步并尝试其他的选择。当我们进行回溯时，可能会发现当前的选择不满足问题的约束条件或无法得到最终的解。这时，我们需要撤销当前的选择，回到上一步进行其他的尝试。

## 经典例题
### 1 入门
#### 1.1 全排列
仓库代码：[全排列](全排列.py)

力扣地址：[46. 全排列](https://leetcode.cn/problems/permutations/description/)

**题目描述**

给定一个不含重复数字的数组nums，返回其所有可能的全排列。

```text
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**套用模板的代码：**
```python
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
```

**解释**
- **终止条件**：根据题目要求，其返回的是全排列的所有可能结果，对于每一个结果都会包含题目所给的所有元素。因此需要选择完所有的元素再终止。
- **路径与选择**
![](https://imgbed-1303886329.cos.ap-nanjing.myqcloud.com/20230609222736.png)
上图对应着路径与选择阶段
  - if语句的作用是判断已排列的元素中是否含有当前元素，全排列是不允许已经被选择的元素再进入。而且题目要求说明了所给数字是不重复的，所以只需要判定已经参与的不再参与就行。后续会介绍所给是有重复的该如何处理。
  - 进入for循环则进入选择阶段，对于第一个candidate(1)，先判断之前是否参与选择，如果没参与则会将1加入选择的列表，选择完后，再进入backtrack函数，进行1之后的元素选择【这个时候if判断就发挥作用了，candidate(1)将不会被选择，而去选择剩余元素】。
  - 当递归结束后，也就得到了排列为1开头的所有全排列。此时需要从选择里面删除1，进入下一个for循环，对2进行搜索。

### 元素无重不可复选
#### 子集

力扣地址：[78. 子集](https://leetcode.cn/problems/subsets/description/)

**题目描述**

给你一个整数数组nums，数组中的元素互不相同 。返回该数组所有可能的子集(幂集)解集。不能包含重复的子集。你可以按任意顺序返回解集。

```text
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**题目理解**

ps:借别人的图一用，懒得画图
思路：按顺序取，只取当前元素后面的元素，即当前元素后面的元素构成候选集。
从根节点开始，题目要求是求子集，先从元素最少的子集开始，也就是空集开始，接下来是空集的子节点。在子节点做选择的时候，可选择的列表有[1,2,3]。
- 第一个子节点，选择1，然后进行递归，在[1]的基础上，生成元素为2的子集，这个时候能选择的列表有[2,3]。所以能够生成两个元素个数为2的子集。
- 在上述生成的子节点的基础上在做选择，因此[1,2]可做的选择只有[3]，生成了[1,2,3]。[1,3]的当前元素是3，3后面没有新的元素，所以不产生新的子集。
![](https://imgbed-1303886329.cos.ap-nanjing.myqcloud.com/20230621175526.png)

**因此代码上需要通过下标来遍历，让下标一直往后移动，直到循环退出**

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        select=[]
        end=len(nums)
        def backtrack(nums,start):
            res.append(select[:])
            for i in range(start,end):
                select.append(nums[i])
                backtrack(nums,i+1)
                select.pop()
        backtrack(nums,0)
        return res
```

#### 组合
力扣地址：[77.组合](https://leetcode.cn/problems/combinations/description/)

**题目描述**

给定两个整数n和k，返回范围[1, n]中所有可能的k个数的组合。 你可以按任何顺序返回答案。

```text
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

**题目理解**

该题与子集的不同之处就在于，对子集的长度进行了要求，因此我们只需要在求子集的基础上加上长度判断即可。

核心思想依旧是将可选择列表当成有序的，只选择未被选择的元素

```python
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
```

### 元素可重不可复选
#### 子集II

力扣地址:[90.子集II](https://leetcode.cn/problems/subsets-ii/description/)

**题目描述**

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 解集不能包含重复的子集。返回的解集中，子集可以按任意顺序排列。

```text
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**题目解释**

ps：继续借图
因为有重复元素，所以首先排序，让重复元素变成相邻的元素，再对其进行预剪枝。需要结合代码理解。
- 剪枝有两个条件，`i>start and nums[i]==nums[i-1]`，其中`i>start`是保证不会删除如图所示的[1,2]后面的子节点[1,2,2]。`num[i]==num[i-1]`是需要在前置条件满足的情况下，剪去相邻重复树枝，而不剪去子节点

![](https://imgbed-1303886329.cos.ap-nanjing.myqcloud.com/20230621193544.png)

**代码**
```python
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
```

#### 组合总和II

力扣地址：[组合总和II](https://leetcode.cn/problems/combination-sum-ii/description/)

**题目描述**

给定一个候选人编号的集合candidates和一个目标数target ，找出candidates中所有可以使数字和为target的组合。 candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 

```text
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**题目解释**

该题中也是包含重复元素，只需要添加一个终止条件`sum(select)==target`即可。

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        select=[]
        candidates.sort()
        def backtrack(nums,start):
            if sum(select)==target:
                res.append(select[:])
                return
            if sum(select)>target:return
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                select.append(nums[i])
                backtrack(nums,i+1)
                select.pop()
        backtrack(candidates,0)
        return res
```

#### 全排列II
 
力扣链接：[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/description/)

**题目描述**
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

```text
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**题目解释**

该题要求全排列、生成的结果不重复。采取的方案是全排列+预剪枝。后剪枝比较耗时。

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        select=[]
        used=[0 for i in nums]
        def backtrack(nums):
            if len(select)==len(nums):
                res.append(select[:])
                return
            for i in range(len(nums)):
                if used[i]==1:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==1:
                    continue
                select.append(nums[i])
                used[i]=1
                backtrack(nums)
                select.pop()
                used[i]=0
        backtrack(nums)
        return res
```

