class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ""
        for ch in s:
            ch=ch.lower()
            if ch.isalnum():
                st+=ch
        return st == st[::-1]