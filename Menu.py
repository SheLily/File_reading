from pprint import pprint

def make_dish(lines):
    '''
    This function creates a dictionary

    '''
    result = {lines[0]: []}
    for i in range(int(lines[1])):
        ind = lines[i + 2].split('|')
        result[lines[0]].append({'ingredient_name': ind[0], 'quantity': int(ind[1]), 'measure': ind[2]})
    return result

def read_file(filename):
    '''
    This function finds out empty strings

    '''
    dishes = {}
    with open(filename) as fin:
        buffer = []
        for line in fin:
            if line == '\n':
                dishes.update(make_dish(buffer))
                buffer = []
            else:
                buffer.append(line[:-1])
    dishes.update(make_dish(buffer))

    return dishes


def get_shop_list_by_dishes(dishes, person_count, recipes={}):
    if len(recipes) == 0:
        recipes.update(read_file('text.txt'))

    shop_list = {}

    for dish in dishes:
        for ind in recipes[dish]:
            if ind['ingredient_name'] in shop_list:
                shop_list[ind['ingredient_name']]['quantity'] += ind['quantity'] * person_count
            else:
                shop_list[ind['ingredient_name']] = {'measure': ind['measure'], 'quantity': ind['quantity']}
                shop_list[ind['ingredient_name']]['quantity'] *= person_count

    return shop_list


shop_list = get_shop_list_by_dishes(('Омлет', 'Фахитос'), 10)

pprint(shop_list)

    

    
    


                
    
