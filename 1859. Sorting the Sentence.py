"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""
def sortSentence(s: str) -> str:
    words = s.split(" ")
    op = [0]*len(words)
    ans = ""
    for each in words:
        op[int(each[len(each)-1])-1] = each[0:len(each)-1]
    for each in op:
        ans += each
        ans += " "
    return ans[0:len(ans)-1]