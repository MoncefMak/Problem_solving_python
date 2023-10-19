class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = []
        max_length = 0
        for char in s:
            if char not in char_index:
                char_index.append(char)
                max_length = max(max_length, len(char_index))
            else:
                index = char_index.index(char)
                char_index[0:index + 1] = []
                char_index.append(char)
        return max_length