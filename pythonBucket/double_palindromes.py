
def check_pal(s):
    return s[::-1] == s

def palindrome_set(lst):
    scores = []
    for word in lst:
        chars = "".join(i for i in word if i.isalpha())
        print(chars)
        nums = "".join(i for i in word if i.isnumeric())
        print(nums)
        score = check_pal(nums) + check_pal(chars)
        scores.append(score)
    return scores