try:
    file = open('taria.txt', 'r')
except FileNotFoundError:
    print('There is no file')
else:
    s = file.read()
    file.close()
