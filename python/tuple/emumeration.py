colors = ['red','orange','yellow']
print(list(enumerate(colors)))


colors = ['red','orange','yellow']
print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index} {value}')