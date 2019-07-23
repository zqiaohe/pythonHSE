n = int(input())
if 10 < n < 20:
    print(str(n) + ' ' + 'korov')
elif n % 10 == 1:
    print(str(n) + ' ' + 'korova')
elif 5 > n % 10 > 1:
    print(str(n) + ' ' + 'korovy')
else:
    print(str(n) + ' ' + 'korov')
