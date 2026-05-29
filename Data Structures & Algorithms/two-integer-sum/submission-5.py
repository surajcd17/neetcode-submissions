class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0,n-1):
            num2 = target - nums[i]
            if num2 in nums: 
                for j in range(i+1,n):
                    if nums[i]+nums[j] == target:
                        return [i,j]
                    else:
                        j = j + 1