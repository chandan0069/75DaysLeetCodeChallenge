class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            comple = target-nums[i]
            if comple in seen:
                return [seen[comple],i]
            seen[nums[i]]=i
        return [-1,-1]
        