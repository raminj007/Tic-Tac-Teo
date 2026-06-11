print("Welcome to Tic-Tac-Toe game")
print("The first number you enter is the row and the second number is the column")
print("")
print("")

def check_statrer():
    while True : 
        x = input("Do you want to start with O or X: ").upper()
        if not (x == "O" or x == "X"): 
            print("Please enter X or O")
        else : 
            return x

def starter():
    import random
    x = random.randint(1, 100)
    y = int(input("Enter a number to decide who starts first = "))
    if x % 2 == 0 and y % 2 == 0:
        print("Great! You start the game")
        return check_statrer() 
    else : 
        print("Your opponent starts with O")
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
        x = input(f"Please enter the desired {s} = ")
        if not x.isdigit():
            print("Please enter a number")
            continue
        elif  x.isdigit() : 
            x_int = int(x)
            if not (1<=x_int<=3):
                print("Please enter a number between 1 and 3")
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
        satr = check_int("row")   
        soton = check_int("column")   
        counter +=1
        if counter %2 == 0 :
            if board[satr-1][soton-1] == " ":
                board[satr-1][soton-1] = y
            elif board[satr-1][soton-1] == "X" or board[satr-1][soton-1] == "O":
                print("This cell is already filled")
                counter -=1
                continue
        else :
            if board[satr-1][soton-1] == " ":
                board[satr-1][soton-1] = x
            elif board[satr-1][soton-1] == "X" or board[satr-1][soton-1] == "O":
                print("This cell is already filled")
                counter -=1
                continue

        display(satr_1,satr_2,satr_3)

        if win_x(*board,counter):
            print("X Wins")
            break
        elif win_o(*board,counter):
            print("O Wins")
            break
        elif counter == 9 :
            print("Draw")
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
    again = input("Do you want to play again? (y/n): ").strip().lower()
    if again == "x":
        print("Ok! see you later")
        break