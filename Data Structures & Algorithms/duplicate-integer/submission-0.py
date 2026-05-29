class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in range(len(nums)):
            for nu in range(num+1,len(nums)):
                if nums[num] == nums[nu]:
                    return True
        return False
        