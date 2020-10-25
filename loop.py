index = 1
fruits = ["Apple", "Bananan", "Orange"]

"""for i in range(6):
    index = index * 2
    print(index)
"""

for i in fruits:
    index = fruits.index(i)
    print("Index of %s is %d" % (i, index))
