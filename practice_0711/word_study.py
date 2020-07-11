word = input().upper()

# ABCC
# alphabets = {"A":1, "B":1, "C":2}
alphabets = {}
for letter in word:
    if letter in alphabets:
        alphabets[letter] +=1
    else: #key값이 없을 때
        alphabets[letter] = 1
alphabets = sorted(alphabets.items(), key=(lambda x:x[1]), reverse=True)
print(alphabets)

if len(word)>1 and alphabets[0][1] == alphabets[1][1]:
    print("?")
else:
    print(alphabets[0][0])