class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem1 = {}
        mem2 = {}

        for char in s:
            if char in mem1:
                mem1[char] = mem1[char] + 1
            else:
                mem1[char] = 1
        
        for char in t:
            if char in mem2:
                mem2[char] = mem2[char] + 1
            else:
                mem2[char] = 1
        
        if mem1 == mem2:
            return True
        return False