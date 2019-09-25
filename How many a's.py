def count(x):
    num = 0
    name = x.lower()
    for item in name:
        if item == "a":
            num = num + 1
    return num

y = input("enter your name: ")
store = count(y)

if store == 1:
    print(y,'has one a in it')
elif store == 0:
    print(y, "has no a's")
else:
    print(y,'has %s a\'s in it' %store)
