arr= ["act", "god", "cat", "dog", "tac"]
dic={}
for i in arr:
    if ''.join(sorted(i)) in dic:
        dic[''.join(sorted(i))].append(i)
    else:
        dic[''.join(sorted(i))]=[i]
print(list(dic.values()))