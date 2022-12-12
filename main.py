
def zad (s):
    a1 = 0
    a2 = 0
    b = 0
    i = 0
    x = s[0]
    y = 0
    z = 0
    while a1 != ':':
        a1 = s[i]
        i += 1
    else:
        j = 1
        b = i
        while j != i - 1:
            x += s[j]
            j += 1
    y = s[i + 2]
    i += 2
    while a2 != '/':
        a2 = s[i]
        i += 1
    else:
        j = b + 3
        while j != i - 1:
            y += s[j]
            j += 1
    z = s[i]
    while i != len(s) - 1:
        i += 1
        z += s[i]
    print(x, y, z)

s = 'https://sait.ru/apo'
zad(s)