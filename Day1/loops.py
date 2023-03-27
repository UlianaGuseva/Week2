# For 
multiplier = 5

for num in range(0, 11):
    print(num * multiplier)

print("Finished")

for num_even in range(0, 51, 2):
    print(num_even)

txt = "Hello there"
for char in txt:
    print(char)
    
# While

# if True:
    # print('hello')

while True:
    print('hello')
    
    
    username = input('usrnm')
    password = input('pswrd')
    
    if username == "yossi":
        break
    elif password == 'Tomato':
        continue
    else:
        print('smth')
        
    tries <3
    username = input('usrnm')
    password = input('pswrd')
    
    if username == "yossi":
        password = input('pswrd')
            if password == 'Tomato':
                print('welcome')
                break
            else:
                tries +=1
                print(f'Tries'+ tries)
    
    