''' This program detects dates in DD/MM/YYYY format.
    Then, it checks if it is a valid date. '''

import re

dateRegex = re.compile(r'''
    ([0][1-9]|[1-2]\d|[3][0-1]) # date digits
    /                           # separator
    ([0][1-9]|[1][0-2])         # month digits
    /                           # separator
    ([1-2]\d\d\d)               # year digits
    ''', re.VERBOSE)

mo = dateRegex.findall('Hello there. Today is 29/02/1204. Tomorrow it will be 13/10/1567. 20/12/2000')
for i in range(len(mo)):
    mo[i] = list(mo[i])
    for j in range(len(mo[i])):
        mo[i][j] = int(mo[i][j])

validDates = []
for i in range(len(mo)):
    validDates.append(True)
    if mo[i][1] == 2:
        if mo[i][0] > 29:
            validDates[i] = False
        elif mo[i][0] == 29:
            if mo[i][2] % 100 == 0:
               if mo[i][2] % 400 != 0:
                   validDates[i] = False
            elif mo[i][2] % 4 != 0:
                validDates[i] = False
    elif mo[i][1] in (4,6,9,11):
        if mo[i][0] == 31:
            validDates[i] = False

for i in range(len(validDates)):
    print(validDates[i])
