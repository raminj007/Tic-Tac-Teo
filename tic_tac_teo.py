print("Be bazi doz (tic tac teo) khosh amadid")
print("Adad avli ke vard mikonid adad satr v adad dovom adad soton mibashad")
print("")
print("")
def check_statrer():
    while True : 
        x = input("Shoma ba O shoro mokonid Ya ba X :   ").upper()
        if not (x == "O" or x == "X"): 
            print("Lotfan X ya O ra vard konid")
        else : 
            return x
def starter():
    import random
    x = random.randint(1, 100)
    y = int(input("Baraye shoro kard bazi va inke che kasi aval shoro kone Yek adad vard konid =   "))
    if x % 2 == 0 and y % 2 == 0:
        print("Eyval! shoma shoro mikonid")
        return check_statrer() 
    else : 
        print("Harif shoma ba O shoro mikonad")
        return check_statrer() 
def display(satr_1,satr_2,satr_3):
    print("")
    print(f" {satr_1[0]} | {satr_1[1]} | {satr_1[2]} ")
    print("-----------")
    print(f" {satr_2[0]} | {satr_2[1]} | {satr_2[2]} ")
    print("-----------") 
    print(f" {satr_3[0]} | {satr_3[1]} | {satr_3[2]} ")
    print("")
def win_x(satr_1,satr_2,satr_3,counter):
    x1 = satr_1[0]== satr_1[1]== satr_1[2]=="X"
    x2 = satr_2[0]== satr_2[1]== satr_2[2]=="X"
    x3 = satr_3[0]== satr_3[1]== satr_3[2]=="X"
    y1 = satr_1[0]== satr_2[0]== satr_3[0]=="X"
    y2 = satr_1[1]== satr_2[1]== satr_3[1]=="X"
    y3 = satr_1[2]== satr_2[2]== satr_3[2]=="X"
    xy1 = satr_1[0]== satr_2[1]== satr_3[2]=="X"
    xy2 = satr_1[2]== satr_2[1]== satr_3[0]=="X"
    return (x1 or x2 or x3 or y1 or y2 or y3 or xy1 or xy2) and counter>=5
def win_o(satr_1,satr_2,satr_3,counter):
    x1 = satr_1[0]== satr_1[1]== satr_1[2]=="O"
    x2 = satr_2[0]== satr_2[1]== satr_2[2]=="O"
    x3 = satr_3[0]== satr_3[1]== satr_3[2]=="O"
    y1 = satr_1[0]== satr_2[0]== satr_3[0]=="O"
    y2 = satr_1[1]== satr_2[1]== satr_3[1]=="O"
    y3 = satr_1[2]== satr_2[2]== satr_3[2]=="O"
    xy1 = satr_1[0]== satr_2[1]== satr_3[2]=="O"
    xy2 = satr_1[2]== satr_2[1]== satr_3[0]=="O"
    return (x1 or x2 or x3 or y1 or y2 or y3 or xy1 or xy2) and counter>=5
def check_int(s):
    while True : 
        x = input(f"Lotafan adad {s} mord nazar ra vard konid =   ")
        if not x.isdigit():
            print("lotfan adad vard konid")
            continue
        elif  x.isdigit() : 
            x_int = int(x)
            if not (1<=x_int<=3):
                print("lotfan adad beyn 1 ta 3 vard konid")
                continue
            else: 
                return x_int
def X_O(x):
    if x =="O" : 
        return "X"
    elif x == "X" : 
        return "O"
def play_game(counter,x,y):
    while True : 
        satr = check_int("satr")   
        soton = check_int("soton")   
        counter +=1
        if counter %2 == 0 : #زوج بودن برای کاربر 1 و اینکه از ایکس استفاده شود
            if board[satr-1][soton-1] == " ":
                board[satr-1][soton-1] = y
            elif board[satr-1][soton-1] == "X" or board[satr-1][soton-1] == "O":
                print("In khone por ast")
                counter -=1
                continue
        else : #فرذ بودن برای کاربر 2 و اینکه از او استفاده شود
            if board[satr-1][soton-1] == " ":
                board[satr-1][soton-1] = x
            elif board[satr-1][soton-1] == "X" or board[satr-1][soton-1] == "O":
                print("In khone por ast")
                counter -=1
                continue
        display(satr_1,satr_2,satr_3)
        if win_x(*board,counter):
            print("Win X")
            break
        elif win_o(*board,counter):
            print("Win O")
            break
        elif counter == 9 :
            print("Draw ")
            break
while True : 
    counter = 0 
    satr_1 = [" "," "," "]
    satr_2 = [" "," "," "]
    satr_3 = [" "," "," "]
    x = starter()
    y = X_O(x)
    board = [satr_1,satr_2,satr_3]
    display(satr_1,satr_2,satr_3)
    play_game(counter,x,y)
    again = input("Mikhay dobare bazi koni ya na (y/n) :  ").strip().lower()
    if again == "x":
        print("Ok! mibinamet badan")
        break
