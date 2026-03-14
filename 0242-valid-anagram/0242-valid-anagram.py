class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for ch in t:
            freq[ord(ch)-ord('a')]-=1
        
        for x in freq:
            if x!=0:
                return False
        return True