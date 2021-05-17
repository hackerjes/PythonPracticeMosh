# names = ['John','Bob', 'Mosh','Sarah','mary']
# print(names[:])
# names[0] = 'Jon'
# print(names)
# exercise
numbers = [10,13, 5, 7, 15, 4, 21, 56,23]
print(min(numbers))
#expert
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
    print(max)