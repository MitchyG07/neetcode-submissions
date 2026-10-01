class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result_arr = []
        counter = 0
        for index, num in enumerate(nums):
            if num != 1:
                result_arr.append(counter)
                counter = 0
            else: 
                counter += 1
                result_arr.append(counter)
        return max(result_arr)