from collections import Counter
filename = 'nameslist.txt'

text_lines = []

with open(filename, 'r') as file:
    while True:
        line= file.readline()
        print(line)
        if line == '':
            break
        
with open(filename, 'r') as file:
    for _ in range(5):
        line= file.readline()
        print(line)
        if line == '':
            break
        
with open(filename, 'r') as file:
        lines= file.readlines(5)
        print(lines)
    
with open(filename, 'r') as file:
        chars= file.readline(5)
        print(chars)
lines = []        
with open(filename, 'r') as file:
    text = file.read()
    text_list = text.split('\n')
    lines= text_list
    
print(lines)

counter = Counter(lines)

print(counter)
print(lines.count('Lea'))
        
        
to_append = '\nUliana\n'
with open(filename, 'a') as file:
    file.write(to_append)

lines_updated = []
for line in lines:
    if line == 'Luke':
        new_line = f'{line} Skywalker'
    else:
        new_line = line
    lines_updated.append(new_line + '\n')
    
    print(lines_updated)
    
    with open(filename, 'a') as file:
        file.writelines(lines_updated)


# with open(filename, 'r') as file:
#     print(file.read())

# with open(filename, 'r') as file:
#     print(file.read(5))
    
# with open(filename, 'r') as file:
#     chars5 = ''
#     for i in range(1, 5):
#         for char in file:
#             chars5 += char
#     print('5 chsrs', chars5)
        
        
    

# # with open(filename, 'r') as file:
# #     print(file.read(5))
    
# # with open(filename, 'r') as file:
# #     text_lines = file.readlines()
# # print(text_lines)

# # with open(filename, 'r') as file:
# #     darth = 0
# #     lea = 0
# #     luke = 0
# #     for line in file:
# #         if line == 'Darth':
# #             darth += 1
# #         elif line == 'Lea':
# #             lea += 1
# #         elif line == 'Luke':
# #             luke +=1
        
# # print(darth, lea, luke)







  