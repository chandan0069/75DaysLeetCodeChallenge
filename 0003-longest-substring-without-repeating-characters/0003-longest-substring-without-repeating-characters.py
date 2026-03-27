class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map={}
        left=0
        max_len=0

        for right in range(len(s)):
            if s[right] in char_map:
                if char_map[s[right]]+1>left:
                    left=char_map[s[right]]+1
            char_map[s[right]]=right

            curr_len = right-left+1
            if curr_len>max_len:
                max_len=curr_len
        
        return max_len