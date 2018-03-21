#https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/

def baum_sweet_sequence(n):
    for i in range(n+1):

        #convert to binary
        l = []
        while i > 0:
            l.append(i%2)
            i = int(i/2)
        binary = l[::-1]

        #look for odd consecutive zero's
        count = 0
        is_bn_1 = True
        for i in binary:
            is_bn_1 = True
            if i == 0:
                count += 1
            else:
                if count%2 == 1:
                    break
        if count%2 == 1:
            is_bn_1 = False
        if is_bn_1:
            print("1\t")
        else:
            print("0\t")

baum_sweet_sequence(20)
