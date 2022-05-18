def checktup(colors, c):
    result = any(c in tup for tup in colors)
    return result

colors = (('Red','White', 'Blue'),('Green', 'Pink', 'Purple'),('Orange', 'Yellow', 'Lime'))
print("Original list:")
print(colors)
c1 = 'White'
print(checktup(colors, c1))

c2 = 'Olive'
print(checktup(colors, c2))
