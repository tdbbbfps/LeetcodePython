def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle in haystack):
                return haystack.find(needle)
        return -1


print(strStr("sadbutsad","sad"))
print(strStr("leetcode","leeto"))