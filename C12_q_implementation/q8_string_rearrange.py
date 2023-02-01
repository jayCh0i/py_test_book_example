n = input()

sum = 0
chars = []

for i in n:
    if i.isdigit():
        sum += int(i)
    else:
        chars.append(i)

chars.sort()

if sum > 0:
    chars += str(sum)

print(''.join(chars))
