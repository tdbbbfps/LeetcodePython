def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        # Define roman to integer rules
        rules = {"I": 1, "V": 5, "X" : 10, "L": 50, "C" : 100, "D" : 500, "M" : 1000}
        extra_rules = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        result = 0
        i = 0
        while i < len(s):
            # First, check if index + 1 is out of range or not. 
            if (i + 1 < len(s)):
                # If not, check if the value of index and index + 1 is in extra rules 
                #             (Combine two characters together)
                combine_value = "".join([s[i], s[i+1]])
                if (combine_value in extra_rules):
                    # print(f"index:{i},{i+1} value:{combine_value} {extra_rules[combine_value]}")
                    result += extra_rules[combine_value]
                    i += 2
                # If it is not in extra rules ,it is converted directly to integer.
                else:
                    # print(f"index:{i} value:{rules[s[i]]}")
                    result += rules[s[i]]
                    i += 1
                        
        return result
# CLEAR VERSION
def _romanToInt(s):
        rules = {"I": 1, "V": 5, "X" : 10, "L": 50, "C" : 100, "D" : 500, "M" : 1000}
        extra_rules = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        result = 0
        i = 0
        while i < len(s):
            if (i + 1 < len(s) and s[i:i+2] in extra_rules):
                result += extra_rules[s[i:i+2]]
                i += 2
            else:
                result += rules[s[i]]
                i += 1
                        
        return result

print(_romanToInt("III"))
print(_romanToInt("LVIII"))
print(_romanToInt("MCMXCIV"))
