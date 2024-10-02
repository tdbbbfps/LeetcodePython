def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        rules = ["()", "[]","{}"]
        i = 0
        x = int(len(s) / 2)
        print(x)
        while i < len(s):
                print(f"{i}: {s[i:x + i]}")
                i += 2 + x
                # if (i + 1 < len(s) and s[i:i+2] in rules):
                #         i += 2
                #         continue
                # else:
                #         return False
        return True


# print(isValid("()"))
# print(isValid("()[]{]"))
# print(isValid("(]"))
print(isValid("([])"))