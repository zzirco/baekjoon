word = input()

data = []
data.append('c=')
data.append('c-')
data.append('dz=')
data.append('d-')
data.append('lj')
data.append('nj')
data.append('s=')
data.append('z=')

count = 0

for i in range(len(data)):
    count += word.count(data[i])
    word = word.replace(data[i], '0')

word = word.replace('0', '')
count += len(word)

print(count)