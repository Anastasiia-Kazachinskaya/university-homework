import pandas as pd
table = pd.read_table('telrecords.csv', ";")
print(table.caller)
caller = list(set(table.caller))
recipient = list(set(table.recipient))
dt = list(set(table.dt))
duration = list(set(table.duration))
print(caller)
print(recipient)
print(dt)
print(duration)
### можно просто вызвать по индексу, так как создали 4 списка и проверив,  что номер имеет индекс [5] просто вызываем элемент по этому же индексу из дургого списка
# myList = ['1', '11', 1, 'a', 'x', 1.1]
# myList.index(1)
# 2
# myList.index('x')
# 4