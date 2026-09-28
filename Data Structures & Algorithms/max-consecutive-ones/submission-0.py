class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        current_count = 0 

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0
    
            if max_num < current_count:
                max_num = current_count

        return max_num