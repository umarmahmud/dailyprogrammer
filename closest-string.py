# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/

def closest_string(nodes, *args):
    weights = {}
    distance_list = []
    
    for a in range(nodes):
        distance = 0
        for b in range(nodes):
            strings = list(zip(args[a], args[b]))
            for i in range(len(strings)):
                for j in range(len(strings[i]) - 1):
                    if strings[i][j] != strings[i][j + 1]:
                        distance += 1
        weights[distance] = args[a]
    
    for k, v in weights.items():
        distance_list.append(k)
    
    return weights[min(distance_list)]