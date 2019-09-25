# Using python for computational needs

restaurant_list = ['banana', 'rice', 'orange', 'pear']

# How many units of each menu item the restaurant has
stock = {
    'banana': 6,
    'orange': 20,
    'apple': 500,
    'pear': 10,
    'beef': 200,
    'chicken': 2,
    'rice': 50
}

# Prices of menu items
prices = {
    'banana': 4,
    'orange': 2,
    'apple': 1.5,
    'pear': 3,
    'beef': 7,
    'chicken': 9,
    'rice': 100
}

def check_order(food): # Checks if there is enough stock to meet customers' orders
    for x in food:
        if stock[x] == 0:
            print(x + ' is out of stock. Please change your order.')
            return False

def compute_bill(food):
    total = 0
    for x in food:
        if stock[x] > 0:
            total += prices[x]
            stock[x] -= 1
    total = str(total)
    return 'That will be ' + total + ' USD please'

if check_order(restaurant_list) != False:
    print(compute_bill(restaurant_list))