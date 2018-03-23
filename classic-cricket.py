class CricketGame:

    def __init__(self, players={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 'Extras': 0}, ball=0, current_batsman=(1,2)):
        self.players = players
        self.ball = ball
        self.current_batsman = current_batsman

    def switch(self): 
        
        batsman_1 = self.current_batsman[0]
        batsman_2 = self.current_batsman[1]
        
        temp = batsman_1 
        batsman_1 = batsman_2
        batsman_2 = temp
    
        return tuple((batsman_1, batsman_2))

    def out(self):
        
        replacement = max(self.current_batsman[0], self.current_batsman[1]) + 1

        return tuple((replacement, self.current_batsman[1]))

    def new_ball(self):
        self.ball += 1
        return self.ball

def main(score):

    game = CricketGame()

    for i in score:
        
        if i.isdigit():
            i = int(i)
            game.players[game.current_batsman[0]] += i
            game.new_ball()
            
            if i%2 == 1:
                game.current_batsman = game.switch()
                
        elif i == '.':
            game.new_ball()

        elif i == 'b':
            game.players['Extras'] += 1
            game.new_ball()
            game.current_batsman = game.switch()

        elif i == 'w':
            if game.ball%6 == 0:
                game.new_ball()
            game.players['Extras'] += 1

        elif i == 'W':
            game.current_batsman = game.out()
            game.new_ball()
        
        if game.ball%6 == 0:
            game.current_batsman = game.switch()

    return game.players

#if __name__ == '__main__'