# https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/

def bookshelf(filename):

    with open(filename, 'r') as f:
        shelves = [int(x) for x in next(f).split()]
        books = 0
        for line in f:
            for i in line.split():
                if i.isdigit():
                    i = int(i)
                    books += i
    
    if books > sum(shelves):
        print('impossible')
        return -1
    
    l = []
    for i in range(len(shelves)):
        count = 1
        for j in range(i, len(shelves)):
            if i != j:
                shelves[i] += shelves[j]
                count += 1
            c = (count, shelves[i] - books)
            if c[1] > 0:
                l.append(c)
                
    minimum, answer = l[0][1], 0
    for i in range(len(l)):
        if l[i][1] < minimum:
            minimum, answer = l[i][1], l[i][0]
            
    return answer
    