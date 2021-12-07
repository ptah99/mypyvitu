cities = ['Nakuru', 'Nairobi', 'Mombasa', 'Kisumu']

# bad way
i = 0
for city in cities:
    print(i, city)
    i += 1

# good way
for i, city in enumerate(cities):
   print(i, city)

#zip
x_list = [1,2,3]
y_list = [2,4,6]
for x, y in zip(x_list, y_list):
    print(x,y)
