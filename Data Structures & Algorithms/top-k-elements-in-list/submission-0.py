class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        countArray = []
        for num, cnt in count.items():
            countArray.append([cnt, num])
        countArray.sort()

        result = []
        while k > 0:
            result.append(countArray.pop()[1])
            k -= 1
        
        return result
            
