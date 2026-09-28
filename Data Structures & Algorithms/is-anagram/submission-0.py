class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = Counter(s)
        print(cnt)
        for c in t:
            if c not in cnt:
                return False
            else: 
                cnt[c] -= 1

        for c in cnt.values():
            if c != 0:
                return False 
        
        return True 
        