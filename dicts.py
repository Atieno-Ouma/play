cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

    result = 0
    basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    for object, count in basket_items.items():
        if object in fruits:
            result += count

    print("There are {} fruits in the basket.".format(result))

    fruit_count, not_fruit_count = 0, 0
    basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    # Iterate through the dictionary
    for object, count in basket_items.items():
        if object in fruits:
            fruit_count += count
        else:
            not_fruit_count += count

    print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

