def plusOne(digits: list[int]) -> list[int]:
    digits[-1] += 1
    i = len(digits) - 1
    # this shit dont work at for val in digits[::-1] the element won't change by iterating
    for val in reversed(digits):
        print(f'index:{i}: {val}')
        if (val >= 10):
            # Check if there's a digit in front this val
            # If not, add one in front
            if (i - 1 >= 0):
                    digits[i -1] += 1
                    digits[i] = 0 
            else:
                digits[i] = 0
                digits.insert(0, 1)
        i -= 1
    return digits

print(plusOne([1,2,3]))
print(plusOne([9]))
print(plusOne([9,9])) #somehow this don't work in leetcode python3 but work on python
print(plusOne([9,9,9,9]))