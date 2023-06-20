def commaCode(theList):
    l = len(theList)
    if l == 0:
        return ''

    s = str(theList[0])

    if l == 1:
        return s
    else:
        for i in range(1,l-1):
            s = s + ', ' + str(theList[i])
        s = s + ', and ' + str(theList[-1])
    return s

s = commaCode([2, 7, 'alpha', 19, 'zoo'])
s1 = commaCode([])
