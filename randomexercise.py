# numbers = {
#     1 : "One",
#     2 : "Two",
#     3 : "Three",
#     4 : "Four",
#     5 : "Five"
# }
# phone = int(input("Phone: "))
# for item in phone:
#     if item == numbers:
#         print(f'{numbers.get()}')
# #Expert
phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2 ": "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, " ! ") + " "
print(output)
