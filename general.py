# Yet another algorithm for the knapsack problem

# === Data ===

# This is the Wikipedia example:
# (https://en.wikipedia.org/wiki/Knapsack_problem) -> Image
items = [
    {'price':4, 'weight':12, 'usage_count':0, 'name':'green'},
    {'price':2, 'weight':1, 'usage_count':0, 'name':'grey'},
    {'price':10, 'weight':4, 'usage_count':0, 'name':'yellow'},
    {'price':1, 'weight':1, 'usage_count':0, 'name':'orange'},
    {'price':2, 'weight':2, 'usage_count':0, 'name':'blue'}
]

# The maximum amount of items we can use later (-1=infinte)
max_item_amount = int(input('What\'s the maximum amout of an item? (-1=infinte)\n'))
# The maximum weight all used items can have
max_weight = 15

# Variables that are being used by helper functions
used_weight = 0
item_index = 0


def main():
    """ That's the main function that will be called at the end """
    # Get rank of each item (price/weight)
    rank_items()
    # Order by rank (from highest to lowest rank)
    order_items()
    # Finally get items to use
    while there_is_an_item():
        if we_can_use_that_item():
            if there_is_place_left_for_that_item():
                use_item()
            else:
                next_item()
        else:
            next_item()
    
    print_result()


#  === Helper functions ===
# These functions are only being used to concentrate more on the algorithm.
# Thats also the reason why I'm using global variables (Sorry for that)


# And don't complain about function names! :D


def rank_items():
    """ Get a rank for each item that is computed by price/weight """
    global items
    
    for item in items:
        item['rank'] = (item['price'] * 1.0) / (item['weight'] * 1.0)  # 1.0 for floats


def order_items():
    """ Order items by rank (from highest to lowest rank) """
    # TODO: What about items[3] and items[4]
    global items
    
    items = sorted(items, key=lambda item:item['rank'], reverse=True)


def there_is_an_item():  # This name will be easier to understand later :D
    """ Return wether we still need to iterate in items """
    global items
    global item_index
    
    return item_index < len(items)


def we_can_use_that_item():  # This name will be easier to understand later :D
    """ Return whether we can use this item. """
    global items
    global max_item_amount
    global item_index
    
    return max_item_amount == -1 or \
           items[item_index]['usage_count'] < max_item_amount


def there_is_place_left_for_that_item():  # This name will be easier to understand later :D
    """ Return whether there is still place left in our knapsack """
    global items
    global used_weight
    global item_index
    global max_weight
    
    return used_weight + items[item_index]['weight'] <= max_weight


def use_item():
    """ Pack item into our knapsack """
    global items
    global item_index
    global used_weight
    
    items[item_index]['usage_count'] += 1
    used_weight += items[item_index]['weight']


def next_item():
    """ Go over to next item """
    global item_index
    
    item_index += 1


def print_result():
    """ Print formatted result """
    global items
    
    print('These are the best items to use:')
    for item in items:
        if item['usage_count'] == 1:
            print('One {}'.format(item['name']))
        elif item['usage_count'] > 1:
            print('{} times {}'.format(item['usage_count'], item['name']))


# We're done, go to main
main()