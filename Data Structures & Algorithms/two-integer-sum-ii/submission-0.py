class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = len(numbers) - 1, 0

        while l > r: 
            dist = numbers[l] + numbers[r]
            if dist > target:
                l -= 1
            if dist < target:
                r += 1 
            if dist == target:
                return [r + 1, l + 1]