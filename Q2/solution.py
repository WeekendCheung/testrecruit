data = []

t = int(input())

for i in range(t):
    data.append(input().split())

allvalid = True
error_msg = ''
for i in range(t):
    if data[i][1] != 'true':
        allvalid = False
        error_msg = error_msg + data[i][2] + ' '

if allvalid == True:
    print("Yes")
else:
    print("No")
    print(error_msg)