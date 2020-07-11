#string
ex_str = "Hi I'm Inji. Lol"
#print(find_idx, index_idx)

#find, index
find_idx = ex_str.find("Inji")
find_result = ex_str.find("Inji")
print(find_idx, find_result)

#find_none = ex_str.index("Piro")
#print(find_none)

try:
    index_none = ex_str.index("Piro")
    print(index_none)
except Exception as e:
    index_none = -1
    print(e)

#split
splitted_str = ex_str.split(" ")
print(splitted_str)

#join
splitted_list = ex_str.split(" ")
joined_str = "-".join(splitted_list)
print(joined_str)

#replace
replaced_str = ex_str.replace("Inji", "Piro")
print(replaced_str)

#strip
text = "      data data          "
print(text.strip())
print(text.replace(" ",""))

#f string (version 3.6 부터)
print(f'{text} 입니다')
name="최인지"
job="프론트엔드"
print("안녕하세요. "+job+" 개발자 "+ name + "입니다.")
print("안녕하세요. {} 개발자 {}입니다.".format(job, name))
print("안녕하세요. {job} 개발자 {name}입니다.".format(job="backend", name="최인지"))
print(f"안녕하세요. {job} 개발자 {name}입니다.")
introductioin = f"안녕하세요. {job} 개발자 {name}입니다."
print(introductioin)

#list
#append, pop, del, remove

#extend
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
def custom_extend(list_1, list_2):
    for item in list_2:
        list_1.append(item)
    return
print(list1)
list3= custom_extend(list1, list2)
print(list1)
print(list3)

#dictionary
ex_dic = {
    "name":"inji",
    "age":25,
    "job":"developer",
}

ex_dic["address"] = "용산"
print(ex_dic)

ex_keys = list(ex_dic.keys())
print(ex_keys)

ex_value = list(ex_dic.values())
print(ex_value)

ex_items = list(ex_dic.items())
print(ex_items)

#lambda

#익명 함수 -> 함수인데 이름이 없다.
#함수 호출 방법 -> 이름을 쓰고 인자를 준다.
#사용 시기:간단한 함수 or 인라인에 사용할 때
#가독성이 떨어지므로 사용 비추

print((lambda x, y: x+y) (1, 2))

#해석
def sum(x, y):
    return x+y
print(sum(1, 2))

#map(function, list) list를 하나씩 돌게 해주고 function 수행하고 결과 반환
#map -> list를 받아서 얘를 function으로 처리한 다음에 result_list를 반환!
numbers = [1, 2, 3, 4, 5]
ex_map_1 = list(map(str, numbers))
print("map 1: ", ex_map_1)
ex_map_2 = list(map(lambda number:number+10, numbers))
print("map 2: ", ex_map_2)
#해석
ex_map_3 = []
def sum10(number):
    return number+10
for number in numbers:
    result = sum10(number)
    ex_map_3.append(result)
print("map 3: ", ex_map_3)

ex_lambda = (lambda x:x+10 if x>10 or x<4 else x-10)
print(ex_lambda(5))
print(ex_lambda(15))

#filter (map과 유사) boolen형 return
ex_filter_1 = list(filter(lambda x: x>3, numbers))
print(ex_filter_1)
#해석
def compare(x):
    return x>3
ex_filter_2 = []
for number in numbers:
    if compare(number):
        ex_filter_2.append(number)
print(ex_filter_2)