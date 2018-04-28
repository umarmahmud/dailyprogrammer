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
    
    print(max_no_of_apple_pies)
    
    if max_no_of_pumpkin_pies > max_no_of_apple_pies:
        majority = 'pumpkin_pies'
        remainder = 'apple_pies'
    elif max_no_of_apple_pies > max_no_of_pumpkin_pies:
        majority = 'apple_pies'
        remainder = 'pumpkin_pies'
    else:
        # if max numbers are tied
        pass
        
    # determine number of ingredients we will need (use dictionary comprehension)
    if majority == 'pumpkin_pies':
        new_dict = {k:v*max_no_of_pumpkin_pies for (k, v) in pumpkin_pie_recipie.items()}
    if majority == 'apple_pies':
        new_dict = {k:v*max_no_of_apple_pies for (k, v) in apple_pie_recipie.items()}
    
    print(available_ingredients)
    print(new_dict)
    
    subtracted_values = list(zip(available_ingredients.values(), new_dict.values()))
    
    print(subtracted_values)
    
    sub_list = []
    
    for i in range(len(subtracted_values)):
        for j in range(1):
            sub_list.append(subtracted_values[i][j] - subtracted_values[i][j + 1])
            
    print(sub_list)
    
    sub_list = dict(zip(available_ingredients, sub_list))
    
    print(sub_list)
    
    if majority == 'pumpkin_pies':
        a = get_max_number(sub_list, pumpkin_pie_recipie)
        print('{} pumpkin pies and {} apple pies'.format(max_no_of_pumpkin_pies, a))
    if majority == 'apple_pies':
        b = get_max_number(sub_list, apple_pie_recipie)
        print('{} apple pies and {} pumpkin pies'.format(max_no_of_apple_pies, b))
    
    print(a)