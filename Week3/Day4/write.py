text = '''1 line\n
ghvjhgv
vghjvj'''

text_list = text.split('\n')
print(text_list)
text_list = ['1 line\n', '\n', 'ghvjhgv\n', 'vghjvj\n']
filename = 'sample.txt'

#w - write
with open(filename, 'w') as file:
    # file.write(text)
    file.writelines(text_list)