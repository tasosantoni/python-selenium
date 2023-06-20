def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        print('Type an integer:')
        value = int(input())
    except ValueError:
        print('You must enter an integer!')
        continue
    if value <= 0:
        print('You must enter a positive integer!')
        continue
    break

while value!= 1:
    value = collatz(value)

