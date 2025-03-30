string = input("Enter some text: ")
count = len(set(string))

print(count > 10)

# or we can use if

# if len(set(string)) > 10:
#     print("True")
# else:
#     print("False")