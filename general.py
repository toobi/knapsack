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


def main(items):
    """ That's the main function that will be called at the end """
    # Get rank of each item (price/weight)
    items = rank_items(items)
    # Order by rank (from highest to lowest rank)
    items = order_items(items)
    # Finally get items to use
    while is_item(items):
        if can_use_item(items):
            if place_left(items):
                use_item(items)
            else:
                next_item()
        else:
            next_item()
    
    print_result()


#  === Helper functions ===

def rank_items(items):
    """ Get a rank for each item that is computed by price/weight """
    for item in items:
        item['rank'] = (item['price'] * 1.0) / (item['weight'] * 1.0)  # I use 1.0 to get floats
    return items


def order_items(items):
    """ Order items by rank (from highest to lowest rank) """
    # TODO: What about items[3] and items[4]
    return sorted(items, key=lambda item:item['rank'], reverse=True)


def is_item(items):
    """ Return whether we still need to iterate in items """
    global item_index
    
    return item_index < len(items)


def can_use_item(items):
    """ Return whether we can use this item. """
    global max_item_amount
    global item_index
    
    return max_item_amount == -1 or \
           items[item_index]['usage_count'] < max_item_amount


def place_left(items):
    """ Return whether there is still place left in our knapsack """
    global used_weight
    global item_index
    global max_weight
    
    return used_weight + items[item_index]['weight'] <= max_weight


def use_item(items):
    """ Pack item into our knapsack """
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
if __name__ == '__main__':
    main(items)