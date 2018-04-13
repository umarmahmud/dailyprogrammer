# https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/

def goldbach_weak_conjecture(*args):
    
    for n in args:
        if n % 2 == 0 or n < 6:
            print("Illegal argument")
            return -1
    
    def find_primes(n):
        l = []
        
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i%j == 0:
                    is_prime = False
            if is_prime:
                l.append(i)
                
        return l
    
    for n in args:
        list_of_primes = find_primes(n)
    
        for i in range(len(list_of_primes)):
            for j in range(i, len(list_of_primes)):
                for k in range(j, len(list_of_primes)):
                    if list_of_primes[i] + list_of_primes[j] + list_of_primes[k] == n:
                        print("{} = {} + {} + {}".format(n, list_of_primes[j], list_of_primes[i], list_of_primes[k]))
                    