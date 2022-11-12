data = []
for i in range(4):
    data.append(input())

order = {'S': -1,
         'M': 0,
         'L': 1}

cloth_num = int(data[0])
request_num = int(data[2])
clothes = data[1].split()
requests = data[3].split()

for i in range(cloth_num):
    num = 1
    if len(clothes[i]) > 1:
        num = len(clothes[i]) - 1
    num = num * order[clothes[i][-1]]
    clothes[i] = num

for i in range(cloth_num):
    for j in range(cloth_num - i - 1):
        if clothes[j] > clothes[j + 1]:
            temp = clothes[j]
            clothes[j] = clothes[j+1]
            clothes[j+1] = temp

flag = 1
for i in range(request_num):
    req = 1
    flag = 0
    if len(requests[i]) > 1:
        req = len(requests[i]) - 1
    req = req * order[requests[i][-1]]
    for j in range(len(clothes)):
        if req <= clothes[j]:
            flag = 1
            clothes.pop(j)
            break
    if flag == 0:
        print("No")
        break
if flag == 1:
    print("Yes")
