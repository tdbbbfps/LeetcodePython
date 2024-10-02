def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 找到最短的字串(最長的CommonPrefix不會超過最短的字串字數)
        min_len = min(len(s) for s in strs)
        prefix = ""
        for i in range(min_len):
                # 以第一個字串的第i個字符作為參考
                current_char = strs[0][i]
                # 檢查所有字串的第i個字符是否相同，若全部相同回傳TRUE 反之結束迴圈 
                if all(s[i] == current_char for s in strs):
                        prefix += current_char
                else:
                        break
        return prefix


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flowen","flow","flowen"])) #最長的CommonPrefix不會超過最短的字串字數 "flow"
print(longestCommonPrefix(["dog","racecar","car"]))