import random
import json

#task1

filename = 'sowpods.txt'
lines = [] 
my_dict = {}
with open(filename, 'r') as file:
    text = file.read()
    text_dict = text.split('\n')
    lines= text_dict
    for i in range(len(lines)):
        my_dict[i] = lines[i]
        
    
# print(len(my_dict))

def get_random_sentence(length):
    sentence = ''
    word = ''
    for i in range(1, int(length)):
       word = random.randint(0, len(my_dict))
       sentence += my_dict[word] + ' '
    print(sentence.lower())
       
get_random_sentence(6)

def main():
    print('I will give you a sentence')
    length = input('print a length of sentence from 2 to 20: ')
    if 2 <= int(length) <=20:
        get_random_sentence(length)
    else:
        print('wrong length of sentence')
    
main()
    
    
# #task2

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payable']['salary'])
data['company']['employee']['birth_date'] = ''
print(data)

json_file = 'my_json.json'

with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj)
    
