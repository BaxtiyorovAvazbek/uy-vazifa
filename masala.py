# 1-masala
series_resistance = ([1, 5, 6, 3])

def func1(series_resistance):
    for RT in series_resistance:
        R1 = 1
        R2 = 5
        R3 = 6
        R4 = 3
        RT = R1 + R2 + R3 + R4
        print(RT, "ohms")
        return series_resistance

func1(series_resistance)

# 2-masala

asc = ([4, 3, 2, 1])
des = ([7, 8, 11, 66])
none = ([1, 2, 3, 4])

def func2(asc,des,none):
    for x in asc:
        asc = ([4, 3, 2, 1])
        des = ([7, 8, 11, 66])
        none = ([1, 2, 3, 4])
        asc.reverse()
        des.reverse()
        print(asc, des, none)
        return asc


func2(asc,des,none)

# 3-masala

def func3(raqam):
    if raqam % 2 == 0:
        yarmi = str(raqam // 2)
        royxat = yarmi
    else:
        yarmi = str(raqam // 2)
        royxat = yarmi

    return royxat


raqam = int(input("Istalgan raqamni kiriting: "))
natija = func3(raqam)
print([natija, natija])

# 4-masala

# 5-masala

def func5(r):
    hisob = {}
    for element in r:
        if element in hisob:
            hisob[element] += 1
        else:
            hisob[element] = 1

    for key, value in hisob.items():
        if value - 2 != 0:
            return key
r = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
natija = func5(r)
print(natija)
# 6-masala

def func6(filter_list):
    for i in filter_list:
        filter_list = ([1, 2, "a", "b"])
        filter_list2 = ([1, "a", "b", 0, 15])
        filter_list3 = ([1, 2, "aasf", "1", "123", 123])
        integer_list = [item for item in filter_list if isinstance(item, int)]
        integer_list2 = [item for item in filter_list2 if isinstance(item, int)]
        integer_list3 = [item for item in filter_list3 if isinstance(item, int)]
        print(integer_list, integer_list2, integer_list3)
        return filter_list

filter_list = ([1, 2, "a", "b"])
filter_list2 = ([1, "a", "b", 0, 15])
filter_list3 = ([1, 2, "aasf", "1", "123", 123])
func6(filter_list)

# 7-masala

# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
#
# print(first)
# print(middle)
# print(last)
# 8-masala

def func8(count_characters):
    characters = 0

    for row in count_characters:
        characters += row.count('#')

    return characters

count_characters = ([
  "###",
  "###",
  "###",
])
natija = func8(count_characters)
print(f"Natija: {natija}")
# 9-masala

def func9(move_to_end):
    for y in move_to_end:
        move = move_to_end.pop(0)
        end = 5
        move_to_end.insert(end, move)
        print(move_to_end)

        return move_to_end


move_to_end = [1, 3, 2, 4, 4, 1]

func9(move_to_end)

# 10-masala