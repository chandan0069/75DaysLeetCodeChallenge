class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq={}
        left=0
        max_freq=0
        max_len=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            if freq[s[right]]>max_freq:
                max_freq=freq[s[right]]

            if right-left+1-max_freq>k:
                freq[s[left]]-=1
                left+=1

            curr_len=right-left+1
            if curr_len>max_len:
                max_len=curr_len
        return max_len