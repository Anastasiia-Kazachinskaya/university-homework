our_str = str(input("Введи строку "))
rows = int(input("Количество строк "))
cols = int(input("Количество столбцов "))

if len(our_str) < rows*cols:
    our_str = our_str + '-'*(rows*cols - len(our_str))
elif len(our_str) > rows*cols:
    our_str = our_str[:rows*cols]
else:
    pass

msg = []
for i in range(rows):
    msg.append([])
    for j in range(cols):
        msg[i].append('-')

print(our_str)

print('Old Matrix')
for i in range(rows):
    for j in range(cols):
        print(msg[i][j], end=' ')
    print()

index_str = 0
for i in range(cols):
    for j in range(rows):
        msg[j][i] = our_str[index_str]
        index_str += 1

print('New Matrix')
for i in range(rows):
    for j in range(cols):
        print(msg[i][j], end=' ')
    print()


