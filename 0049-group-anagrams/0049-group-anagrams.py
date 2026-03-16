class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for word in strs:

            count = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result = []

        for k in groups:
            result.append(groups[k])

        return result