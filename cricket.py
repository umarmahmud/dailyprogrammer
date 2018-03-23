#https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/

def cricket(score):
    
    players = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 'Extras': 0}
    ball = 0
    current_batsman = (1, 2)
    dot = '.'
    bye = 'b'
    wide = 'w'
    wicket = 'W'

    def switch():
    
        batsman_1 = current_batsman[0]
        batsman_2 = current_batsman[1]
    
        temp = batsman_1
        batsman_1 = batsman_2
        batsman_2 = temp
    
        return tuple((batsman_1, batsman_2))

    def out():
        
        replacement = max(current_batsman[0], current_batsman[1]) + 1
        return tuple((replacement, current_batsman[1]))
        
    for i in score:
        
        if i.isdigit():
            i = int(i)
            players[current_batsman[0]] += i
            ball += 1
            
            if i%2 == 1:
                current_batsman = switch()
                
        elif i == dot:
            ball += 1

        elif i == bye:
            players['Extras'] += 1
            ball += 1
            current_batsman = switch()

        elif i == wide:
            if ball%6 == 0:
                ball += 1
            players['Extras'] += 1

        elif i == wicket:
            current_batsman = out()
            ball += 1
        
        if ball%6 == 0:
            current_batsman = switch()
            
    return players

            
