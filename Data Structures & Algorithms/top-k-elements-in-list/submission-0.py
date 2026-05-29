from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count_list = []
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count +=  1
            else :
                count_list.append((nums[i-1],count))
                count = 1
        count_list.append((nums[-1],count))
        count_list.sort(key = lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(count_list[i][0])
        return result
        