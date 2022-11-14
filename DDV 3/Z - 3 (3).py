n = int(input())
mins = n
hours = mins // 60
mins = n % 60
if n < 1440:
    print(hours,':', mins)
else:
    days = hours // 24
    hours %= 24
    print(days, 'сут.', hours, ':', mins)