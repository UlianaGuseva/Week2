filename = 'sample.txt'

text = ''
text_lines1 = []
text_lines2 = []

with open(filename, 'r') as file:
    # print(file.read())
    # text = file.read()
    text_lines1 = file.readlines()
    file.seek(0)
    text_lines2 = file.readlines()
    
    
print(text_lines1)
print(text_lines2)


