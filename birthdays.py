import pprint

message = 'It was a bright cold day in Aprin, and the clocks were striking \
thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
