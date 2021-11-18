points = 174

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)


for i in range(3):
    print("Hello!")
#range(start=0, stop, step=1)
range(1, 10, 2)

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

    names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
    usernames = []

    for name in names:
        usernames.append(name.lower().replace(" ", "_"))

    print(usernames)

    usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

    for i in range(len(usernames)):
        usernames[i] = usernames[i].lower().replace(" ", "_")

    print(usernames)

    tokens = ['<greeting>', 'Hello World!', '</greeting>']

    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1

    print(count)