# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
from collections import OrderedDict

def number_of_pies(ingredients):
    pumpkin_pie_recipie = {'pumpkin-flavoring': 1,
                   'eggs': 3,
                   'milk': 4,
                   'sugar': 3
                  }
    apple_pie_recipie = {'apples': 1,
                 'eggs': 4,
                 'milk': 3,
                 'sugar': 2
                }
    available_ingredients = {'pumpkin-flavoring': 0,
                            'apples': 0,
                            'eggs': 0,
                            'milk': 0,
                            'sugar': 0
                            }
    
    # add ingredients array (the input) to dictionary values
    available_ingredients = dict(zip(available_ingredients, ingredients))
    
    # count number of pumpkin pies we can make
    
    # copy as not to modify original dictionary
    pumpkin_pies = available_ingredients.copy()
    
    pumpkin_pies.pop('apples')
    
    pumpkin_pies = tuple(zip(pumpkin_pies.values(), pumpkin_pie_recipie.values()))
    
    print(pumpkin_pies)
    
    pumpkin_quotient = []
    
    for i in range(len(pumpkin_pies)):
        for j in range(1):
            pumpkin_quotient.append(int(pumpkin_pies[i][j]/pumpkin_pies[i][j+1]))
    
    print(min(pumpkin_quotient))
                  
    # count number of apple pies we can make
    
    #copy as not to modify original dictionary
    apple_pies = available_ingredients.copy()
    
    apple_pies.pop('pumpkin-flavoring')
    
    apple_pies = tuple(zip(apple_pies.values(), apple_pie_recipie.values()))
    
    print(apple_pies)
    
    apple_quotient = []
    
    for i in range(len(apple_pies)):
        for j in range(1):
            apple_quotient.append(int(apple_pies[i][j]/apple_pies[i][j+1]))
            
    print(min(apple_quotient))
    
    # take both counts of pies, take larger value. After that, subtract ingredients used for larger value pie and see max number
    # of other kind of pie that can be made with remaining ingredients
    