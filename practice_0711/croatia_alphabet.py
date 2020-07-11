word = input()
croatias = ("c=","c-","dz=","d-","lj","nj","s=","z=")

#ljc-aaa => 5 lj->1, c->1
#00aaa => len(word):5

for croatia in croatias:
    word = word.replace(croatia, "0")
print(len(word))