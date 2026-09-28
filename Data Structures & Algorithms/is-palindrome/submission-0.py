class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        string = s.replace(" ", "")
        j = len(string) - 1

        while i < j:
            if not string[i].isalnum():
                i += 1 
                continue
            print(j)
            if not string[j].isalnum():
                j -= 1
                continue
            if string[i].lower() != string[j].lower():
                return False
            i += 1
            j -= 1
        
        return True
