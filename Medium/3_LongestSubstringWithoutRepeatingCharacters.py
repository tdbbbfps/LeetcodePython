def lengthOfLongestSubstring(s: str) -> int:
        substring = []
        temp_substring = ""
        dup_idx = 0
        for i in s:
        # Check if there's any duplicates in temp_substring
            if (not i in temp_substring):
                temp_substring += i
        # If there's duplicate then put it in substring and remove all the elements in front of the duplicate(included)
            elif (i in temp_substring):
                dup_idx = temp_substring.index(i)
                substring.append(temp_substring)
                temp_substring = temp_substring[dup_idx + 1:] + i
        substring.append(temp_substring)
        print(substring)
        return max(len(s) for s in substring)

print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("jbpnbwwd"))
print(lengthOfLongestSubstring("bbbcdefg"))