class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexBySum = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexBySum:
                return [indexBySum[diff], i]
            else:
                indexBySum[nums[i]] = i