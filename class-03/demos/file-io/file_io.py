
# We need to read assets/spam.txt. What to do?

# file = open('assets/spam.txt')

# # print(spam)

# content = file.read()

# print(content)

# print('Is file closed?', file.closed)

# file.close()
# print('Is file closed?', file.closed)


with open('assets/spam.txt') as file:
    print(file.read())

print('file is closed?', file.closed)



with open('assets/brain.jpg','rb') as file:
    contents = file.read()


# for x in contents[:128]:
#     print(type(contents))

trimmed = contents[:len(contents) // 2]


with open('assets/brain.copy.jpg', 'wb') as f2:
    f2.write(trimmed)
