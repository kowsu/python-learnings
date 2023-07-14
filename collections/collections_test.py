numbers = [11, 12, 14, 13]

print(numbers[0])
print(numbers[1])
print(numbers[3])

print(len(numbers))
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])

print(14 in numbers)


point = (3, 5, 6, 7)
print(point[0])
print(point[1])


x, y, z, a = point

print(a)
print(z)
