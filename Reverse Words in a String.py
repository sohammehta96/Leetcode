"""
Given a String S, reverse the string without reversing its individual
words. Words are separated by dots.
"""
def reversewords(s):
    string = s.split(".")
    result = ""
    for i in range(len(string)):
        result = result + string[len(string)-1-i] + "."
    return result

s = "i.like.this.program.very.much"
print(reversewords(s))