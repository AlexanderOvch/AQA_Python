lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum1 = sum([item for item in lst1 if item % 2 == 0])
print(sum1)

# або можемо через if
# sum1 = 0
# for item in lst1:
#     if item % 2 == 0:
#         sum1 += item
# print(sum1)