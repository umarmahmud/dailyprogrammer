# https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/

my_books = 700
shelves = [200, 300, 250, 300]
l = []

for i in range(len(shelves)):
    count = 1
    for j in range(i, len(shelves)):
        print(shelves[i], shelves[j])
        if i != j:
            shelves[i] += shelves[j]
            count += 1
        c = (count, shelves[i] - my_books)
        l.append(c)
        print(shelves[i])
    print("-------")
print(l)

for i in range(len(l)):
    if l[i][1] >= 0:
        minimum, answer = l[i][1], 0
        if l[0][1] < minimum:
            minimum, answer = l[i][1], l[i][0]
print(answer)