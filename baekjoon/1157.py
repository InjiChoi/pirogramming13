word = input()

s = list(word.lower())

alpha = list(set(s)) # 사용된 알파벳

cnt = {} # 사용된 횟수

for i in range(len(alpha)):
    cnt[alpha[i]] = s.count(alpha[i])
    
result = []

for key in cnt.keys():
    if cnt[key] == max(cnt.values()):
        result.append(key)

if len(result) > 1:
    print('?')
else:
    print(result[0].upper())
