number = [1, 2, 3, 4, 5, 6]

i = 0
highest = 0
while i < len(number):
    if number[i] > highest:
        highest = number[i]
    i += 1

print(highest)

# Another way, both are good

max = number[0]
for num in number:
    if num > max:
        max = num

print(max)
