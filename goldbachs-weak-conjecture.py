def goldbach_weak_conjecture(n):
    
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
    
    list_of_primes = find_primes(n)
    sum_list = []
    
    for i in range(len(list_of_primes)):
        for j in range(i, len(list_of_primes)):
            for k in range(j, len(list_of_primes)):
                if list_of_primes[i] + list_of_primes[j] + list_of_primes[k] == n:
                    sum_list.append(list_of_primes[i])
                    sum_list.append(list_of_primes[j])
                    sum_list.append(list_of_primes[k])
                    sum_list.append("-------")
                    
    return sum_list
