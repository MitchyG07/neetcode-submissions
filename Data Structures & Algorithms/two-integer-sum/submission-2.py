class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexByDiff = {}
        for i in range(len(nums)):
            indexByDiff[nums[i]] = i
        
        print(indexByDiff)

        for i in range(len(nums)):
            currIndex = indexByDiff[nums[i]]
            diff = target - nums[i]

            if diff in indexByDiff and indexByDiff[diff] != i:
                return [i, indexByDiff[diff]]

        return []