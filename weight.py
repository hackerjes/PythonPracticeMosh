
# weight = int(input("enter your weight: "))
# type = input("(L)bs or (K)g: ")
# if type == 'K':
#     pounds = weight * 0.45
#     kpounds = f'You are  {pounds} pounds'
#     print(kpounds)
# else type == 'L':
#     kilogram = weight / 0.45
#     kgrams = f'You are {kilogram} kilograms'
#     print(kgrams)

#expert
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
