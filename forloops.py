prices = [10,20,30]
total = 0
for price in prices:
    total += price
    print (f"The total is : {total} ")

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
#challenge 
# numbers = [5, 2 , 5, 2, 2]
# i = 0
# for i in numbers:
#     print('x'* i)
#expert
numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
