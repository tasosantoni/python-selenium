allGuests = {'Alice': {'apples': 5, 'pretzels':12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups':3, 'apple pies':1}}


def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought += v.get(item,0)
    return numBrought

print('Number of things brought:')
print(str(totalBrought(allGuests, 'apples')) + ' apples')
print(str(totalBrought(allGuests, 'pretzels')) + ' pretzels')
print(str(totalBrought(allGuests, 'ham sandwiches')) + ' ham sandwiches')
print(str(totalBrought(allGuests, 'cups')) + ' cups')
print(str(totalBrought(allGuests, 'apple pies')) + ' apple pies')
