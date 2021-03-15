import csv

filepath = r"c:/Users/Mike/PycharmProjects/tasks/text.csv"

arr2 = []

dict_count = {}


with open(filepath, "r", newline="") as file:
    #читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        cur_arr = row[0].split(":")
        tmp = cur_arr[1]
        arr2.append(tmp)

# print(arr2)

for s in arr2:
    if s in dict_count.keys():
        dict_count[s] += 1
    else:
        dict_count[s] = 1


sorted_dict = {}
sorted_keys = sorted(dict_count, key=dict_count.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = dict_count[w]

for i in sorted_dict:
    print(i, ":", sorted_dict[i])