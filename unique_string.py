str_ = "Hi Hi Hi mike mike you to to mike to to to to"

word_list = str_.split(" ")
not_sorted_dict = {}

for s in word_list:
    if s in not_sorted_dict.keys():
        not_sorted_dict[s] += 1
    else:
        not_sorted_dict[s] = 1


sorted_dict = {}
sorted_keys = sorted(not_sorted_dict, key=not_sorted_dict.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = not_sorted_dict[w]

print(list(sorted_dict.keys()))


