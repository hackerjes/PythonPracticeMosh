# numbers = [1, 2, 3, 3, 4, 5, 6, 7]
# numbers2 = numbers
# previous_item= numbers2.index()
# for item in numbers2:
#     if item == previous_item:
#         numbers2.remove()
#     else:
#         previous_item +=1
    
# print(numbers)
# print(numbers2)
# Expert
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)