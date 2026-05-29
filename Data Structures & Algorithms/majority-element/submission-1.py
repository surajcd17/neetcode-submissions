class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums= sorted(nums)
        max_count = 0
        max_num =0
        i = 0
        while i < len(nums):
            count = 1
            num = nums[i]
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                else:
                    break 
            if count > max_count :
                max_num = num 
                max_count = count
            i += count
        return max_num