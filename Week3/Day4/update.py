filename = 'sample.txt'

text_lines = []
with open(filename, 'r') as file:
    text_lines = file.readlines()
    
print(text_lines)

new_str = 'hvjhgtyjfy\n'

text_lines.insert(2, new_str)

print(text_lines)

with open(filename, 'w') as file:
    text_lines = file.writelines(text_lines)
    

