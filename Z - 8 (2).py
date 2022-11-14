strok = 'Я строчка строчка строчка я вовсе не медведь'.lower().split(' ')
for i in range(len(strok)):
    strok[i] = ''.join(sorted(strok[i]))
print(' '.join(strok))