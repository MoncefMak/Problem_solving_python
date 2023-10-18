class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastsubstring = substring = ""
        index = 0

        while index < len(s):
            for value in range(index, len(s)):
                if s[value] not in substring:
                    substring += s[value]
                else:
                    index += 1
                    if len(substring) > len(lastsubstring):
                        lastsubstring = substring
                        substring = ""
                        break
        return len(lastsubstring)
