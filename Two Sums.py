class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = {}
        for index, num in enumerate(nums):

            if target - num in prevs:
                return [prevs[target - num], index]
            prevs[num] = index
