class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high = len(nums)-1
        ans = (2**31)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans = min(nums[mid],ans)
                high = mid-1
        return ans