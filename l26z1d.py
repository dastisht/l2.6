def check (d, m, y):
    
    if y < 1 or y > 9999:
        return False
    if m > 12:
        return False
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8  or m == 10  or m == 12:
        if d > 31 or d < 0:
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
         if d > 30 or d < 0:
            return False
    elif m == 2:
        if w_chek(y) == True:
            if d > 29 or d < 0:
                return False
        elif w_chek(y) == False:
            if d > 28 or d < 0:
                return False
    return True
def w_chek (y):
    if y % 4 == 0 or y % 100 == 0 and y % 400 != 0:
        return  True
    return False
d = int(input("Введите день: "))
m = int(input("Введите месяц: "))
y = int(input("Введите год: "))

def p_data():
    res = check(d,m,y)
    if res == True:
        print("Дата существует")
    else:
        print("Дата не существует")
        