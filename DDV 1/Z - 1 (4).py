seconds = int(input())
mins = seconds // 60
print('Минут = ', mins)
if mins < 60 :
    print('Часов = 0')
    print('Дней = 0')
else :
    hours = mins // 60
    print('Часов = ', hours)
    if hours < 24:
        print('Полных Дней = 0')
    else:
        days = hours // 24
        print('Полных Дней = ', days)

