# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
from collections import OrderedDict

def number_of_pies(ingredients):
    pumpkin_pie_recipie = {'pumpkin-flavoring': 1,
                           'apples': 0,
                           'eggs': 3,
                           'milk': 4,
                           'sugar': 3
                          }
    apple_pie_recipie = {'pumpkin-flavoring': 0,
                         'apples': 1,
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
    
    # get max number of pumpkin/apple pies we can make
    def get_max_number(ingredients, recipie):
        pies = tuple(zip(ingredients.values(), recipie.values()))
        quotient = []

        for i in range(len(pies)):
            for j in range(1):
                if pies[i][j+1] == 0:
                    continue
                quotient.append(int(pies[i][j]/pies[i][j+1]))

        return min(quotient)
    
    max_no_of_pumpkin_pies = get_max_number(available_ingredients, pumpkin_pie_recipie)
    max_no_of_apple_pies = get_max_number(available_ingredients, apple_pie_recipie)
    
    if max_no_of_pumpkin_pies > max_no_of_apple_pies:
        majority = 'pumpkin_pies'
        remainder = 'apple_pies'
    elif max_no_of_apple_pies > max_no_of_pumpkin_pies:
        majority = 'apple_pies'
        remainder = 'pumpkin_pies'
    else:
        # if max numbers are tied
        pass
        
    # determine number of ingredients we will need
    if majority == 'pumpkin_pies':
        for k, v in pumpkin_pie_recipie.items():
            v *= max_no_of_pumpkin_pies
            print(k, v)
            
        print(remainder)
        
    # subtract values, determine max number of other kind of pie that can be made with remaining ingredients
    