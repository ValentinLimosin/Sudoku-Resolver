def affiche(tabl):
    print("-----------------------------------")
    for y in range(0, 9, 1):
        print(tabl[y][0],"|",tabl[y][1],"|",tabl[y][2],"|",tabl[y][3],"|",tabl[y][4],"|",tabl[y][5],"|",tabl[y][6],"|",tabl[y][7],"|",tabl[y][8],"|")
        print("-----------------------------------")

def start(tabl, x, y):
    i = 1
    if (x == 8 and y == 8):
        return(True);
    if tabl[y][x] != str(0):
        if (x == 8):
            return(start(tabl, 0, y + 1));
        else:
            return(start(tabl, x + 1, y));
    for i in range(1, 10, 1):
        if (chekline(tabl, i, y) and chekcolon(tabl, i, x) and checksqarre(tabl, i, x, y)):
            tabl[y][x] = str(i)
            if (x == 8):
                if (start(tabl, 0, y + 1)):
                    return (True); 
            else:
                if (start(tabl, x + 1, y)):
                    return(True);
    tabl[y][x] = str(0)
    return(False);


def chekline(tabl, i, y):
    for x in range(0, 9, 1):
        if tabl[y][x] == str(i):
            return(False);
    return(True);

def chekcolon(tabl, i, x):
    for y in range(0, 9, 1):
        if tabl[y][x] == str(i):
            return(False);
    return(True);

def checksqarre(tabl, i, x, y):
    xa = x - (x % 3)
    ya = y - (y % 3)
    for y in range(ya, ya + 3, 1):
        for x in range(xa, xa + 3, 1):
            if (tabl[y][x] == str(i)):
                return(False);
    return(True);


print("/I\INFO/I\ pour des endroit vide placé un 0")
tabl = [[0] * 9 for _ in range(9)]
tabl[0] = list(input("entré la première ligne  :"))
tabl[1] = list(input("entré la deuxieme ligne  :"))
tabl[2] = list(input("entré la trosieme ligne  :"))
tabl[3] = list(input("entré la quatrieme ligne :"))
tabl[4] = list(input("entré la cinquieme ligne :"))
tabl[5] = list(input("entré la sixième ligne   :"))
tabl[6] = list(input("entré la septième ligne  :"))
tabl[7] = list(input("entré la huitième ligne  :"))
tabl[8] = list(input("entré la neuvième ligne  :"))
print("vous avez entré:")
affiche(tabl)
start(tabl, 0, 0)
print("Le resultat est")
affiche(tabl)
