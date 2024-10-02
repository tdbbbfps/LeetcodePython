def lengthOfLastWord(s: str) -> int:
    s = s.split()
    s = s[len(s) - 1]
    return len(s)
    # With just one line: 
    # return len(s.split()[-1]) 

print(lengthOfLastWord("Hello world!"))
print(lengthOfLastWord("   fly me   to   the moon  "))