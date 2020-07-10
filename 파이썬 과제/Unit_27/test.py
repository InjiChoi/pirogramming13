with open('words.txt','r') as file:
    words = file.readlines()
str = words[0].split()
for i in range(len(str)):
    if 'c' in str[i]:
        print(str[i].strip(',.'))
