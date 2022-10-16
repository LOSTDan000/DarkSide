mins=int(input())
hrs=0
if mins>59 :
    while mins>59 :
        mins = mins - 60
        hrs = hrs + 1
elif mins<59 :
    mins = mins
print(hrs,'Hours')
print(mins,'Minutes')