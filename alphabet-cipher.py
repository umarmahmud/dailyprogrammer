# https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

def alphabet_cipher(secret, message):
    
    s = 'abcdefghijklmnopqrstuvwxyz'
    
    #match length of secret with length of message
    secret_match = []

    for i in range(int(len(message)/len(secret))):
        for j in secret:
            secret_match.append(j)

    trailing = secret[:len(message)%len(secret)]

    for i in trailing:
        secret_match.append(i)
        
    # letters in tabula recta
    letters = []
    
    for i, j in enumerate(s):
        for k in s[i:]:
            letters.append(k)
        for l in s[:i]:
            letters.append(l)
        
    # "keys" of tabula recta
    keys = []

    for a in s:
        for b in s:
            keys.append([a,b])

    # create tabula recta
    tabula_recta = list(zip(keys, letters))
    
    # zip message and secret for encoding
    to_encode = list(zip(secret_match, message))
    
    encoded_message = ''

    # encode
    for m in to_encode:
        for i, j in enumerate(tabula_recta):
            for k in range(1):
                if list(m) == tabula_recta[i][k]:
                    encoded_message += str(tabula_recta[i][1])
                    
    return encoded_message