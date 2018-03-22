#https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/

def number_of_hours(list_of_times):

    hours_set = set()

    for i, j in enumerate(list_of_times):
        start, end = list_of_times[i]
        for k in range(start, end):
            hours_set.add(k)

    return len(hours_set)

print(number_of_hours([(15,8), (13,16), (9,12), (3,4), (17,20), (9,11), (17,18), (4,5), (5,6), (4,5), (5,6), (13,16), (2,3), (15,17), (13,14)]))
print(number_of_hours([(2,5),(1,3),(8,10),(7,9),(1,5)]))
