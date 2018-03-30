# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

def integer_complexity(n):
    l = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            if i * j == n:
                l.append(i + j)
    return min(l)