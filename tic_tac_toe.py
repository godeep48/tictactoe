import random
from IPython.display import clear_output
player = "X"
computer = "O"

'''
The below code will display the output in most conventional TUI form.
'''
num = [" "]*9
def print_output():
    print(" ", "|", " ", "|")
    print(num[0], "|",num[1], "|",num[2])
    print(" ", "|", " ", "|")
    print("---------")
    print(" ", "|", " ", "|")
    print(num[3],"|",num[4],"|",num[5])
    print(" ", "|", " ", "|")
    print("---------")
    print(" ", "|", " ", "|")
    print(num[6],"|",num[7],"|",num[8])
    print(" ", "|", " ", "|")
    
    
import random
new_list = [0,2,6,8]

'''
Attack code starts here. 
'''
def computer_turn():


    if num[0]==num[1]==computer and (num[2] != "X" and num[2] != "O"):
        num[2] = x.pop(0)
        print("24")
        
    elif num[1]==num[2]==computer and (num[0] != "X" and num[0] != "O"):
        num[0] = x.pop(0)
        print("25")
        
    elif num[3]==num[4]==computer and (num[5] != "X" and num[5] != "O"):
        num[5] = x.pop(0)
        print("26")
        
    elif num[4]==num[5]==computer and (num[3] != "X" and num[3] != "O"):
        num[3] = x.pop(0)
        print("27")
        
    elif num[6]==num[7]==computer and (num[8] != "X" and num[8] != "O"):
        num[8] = x.pop(0)
        print("28")
        
    elif num[7]==num[8]==computer and (num[6] != "X" and num[6] != "O"):
        num[6] = x.pop(0)
        print("29")
        
    elif num[0]==num[3]==computer and (num[6] != "X" and num[6] != "O"):
        num[6] = x.pop(0)
        print("30")
        
    elif num[3]==num[6]==computer and (num[0] != "X" and num[0] != "O"):
        num[0] = x.pop(0)
        print("31")
        
    elif num[1]==num[4]==computer and (num[7] != "X" and num[7] != "O"):
        num[7] = x.pop(0)
        print("32")
        
    elif num[4]==num[7]==computer and (num[1] != "X" and num[1] != "O"):
        num[1] = x.pop(0)
        print("33")
        
    elif num[2]==num[5]==computer and (num[8] != "X" and num[8] != "O"):
        num[8] = x.pop(0)
        print("34")
        
    elif num[5]==num[8]==computer and (num[2] != "X" and num[2] != "O"):
        num[2] = x.pop(0)
        print("35")
        
    elif num[0]==num[6]==computer and (num[3] != "X" and num[3] != "O"):
        num[3] = x.pop(0)
        print("36")
        
    elif num[1]==num[7]==computer and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("37")
        
    elif num[2]==num[8]==computer and (num[5] != "X" and num[5] != "O"):
        num[5] = x.pop(0)
        print("38")
        
    elif num[0]==num[2]==computer and (num[1] != "X" and num[1] != "O"):
        num[1] = x.pop(0)
        print("39")
        
    elif num[3]==num[5]==computer and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("40")
        
    elif num[6]==num[8]==computer and (num[7] != "X" and num[7] != "O"):
        num[7] = x.pop(0)
        print("41")
        
    elif num[0]==num[8]==computer and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("42")
        
    elif num[2]==num[6]==computer and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("43")

    elif num[0]==num[8]==computer and (num[4]==player):
        for d in (0,2,6,8):
            if num[d]!=player and num[d]!=computer:
                num[d]=x.pop(0)
                print("100")
            else:
                pass
        
    elif len(x)==7 and num[4] == player:
        if num[2]==computer:
            num[6] = x.pop(0)
            print("47")
            
        elif num[0]==computer:
            num[8] = x.pop(0)
            print("48")
            
        elif num[6]==computer:
            num[2] = x.pop(0)
            print("49")
            
        elif num[8]==computer:
            num[0] = x.pop(0)
            print("50")
            
        
    elif len(x)==7 and (num[0] or num[1] or num[2] or num[3] or num[5] or num[6] or num[7] or num[8])==player:
        if num[0] == computer:
            for a in (2,6):
                if num[a]!="X" and num[a]!="O":
                    num[a] = x.pop(0)
                    print("51")
                    
                    break
                else:
                    pass
        elif num[2] == computer:
            for a in (6,8):
                if num[a]!="X" and num[a]!="O":
                    num[a] = x.pop(0)
                    print("52")
                    
                    break
                else:
                    pass
        elif num[8] == computer:
            for a in (6,2):
                if num[a]!="X" and num[a]!="O":
                    num[a] = x.pop(0)
                    print("53")
                    
                    break
                else:
                    pass
        elif num[6] == computer:
            for a in (8,0):
                if num[a]!="X" and num[a]!="O":
                    num[a] = x.pop(0)
                    print("54")
                    
                    break
                else:
                    pass
        
    elif len(x)==9:
        rand_num = random.choice(new_list)
        num[rand_num] = x.pop(0)
        print("44")
        
        
    elif len(x)==5:
        if num[0] == num[2]:
            for b in (6,8):
                if num[b]!="X" and num[b]!="O":
                    num[b] = x.pop(0)
                    print("55")
                    
                    break
                else:
                    pass
        elif num[2] == num[8]:
            for b in (0,6):
                if num[b]!="X" and num[b]!="O":
                    num[b] = x.pop(0)
                    print("56")
                    
                    break
                else:
                    pass
        elif num[8] == num[6]:
            for b in (0,2):
                if num[b]!="X" and num[b]!="O":
                    num[b] = x.pop(0)
                    print("57")
                    
                    break
                else:
                    pass
        elif num[0] == num[6]:
            for b in (2,8):
                if num[b]!="X" and num[b]!="O":
                    num[b] = x.pop(0)
                    print("58")
                    
                    break
                else:
                    pass
    elif len(x)==7 and (num[0]==computer or num[2]==computer or num[6]==computer or num[8]==computer) and\
        num[4]!="X" and num[4]!="O":
            for c in (0,2,6,8):
                if num[c]!="X" and num[c]!="O":
                    num[c] = x.pop(0)
                    print(f"Edited {c}")
                    
                    break
                else:
                    pass

# Attack code ends here
###################################################################


    elif num[0]==num[1]==player and (num[2] != "X" and num[2] != "O"):
        num[2] = x.pop(0)
        print("1")
        
    elif num[1] == num[2] == player and (num[0] != "X" and num[0] != "O"):
        num[0] = x.pop(0)
        print("2")
        
    elif num[3] == num[4] == player and (num[5] != "X" and num[5] != "O"):
        num[5] = x.pop(0)
        print("3")
        
    elif num[4] == num[5] == player and (num[3] != "X" and num[3] != "O"):
        num[3] = x.pop(0)
        print("4")
        
    elif num[6] == num[7] == player and (num[8] != "X" and num[8] != "O"):
        num[8] = x.pop(0)
        print("5")
        
    elif num[7] == num[8] == player and (num[6] != "X" and num[6] != "O"):
        num[6] = x.pop(0)
        print("6")
        
    elif num[0] == num[3] == player and (num[6] != "X" and num[6] != "O"):
        num[6] = x.pop(0)
        print("7")
        
    elif num[1] == num[4] == player and (num[7] != "X" and num[7] != "O"):
        num[7] = x.pop(0)
        print("8")
        
    elif num[2] == num[5] == player and (num[8] != "X" and num[8] != "O"):
        num[8] = x.pop(0)
        print("9")
        
    elif num[0] == num[6] == player and (num[3] != "X" and num[3] != "O"):
        num[3] = x.pop(0)
        print("10")
        
    elif num[1] == num[7] == player and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("11")
        
    elif num[2] == num[8] == player and (num[5] != "X" and num[5] != "O"):
        num[5] = x.pop(0)
        print("12")
        
    elif num[0] == num[2] == player and (num[1] != "X" and num[1] != "O"):
        num[1] = x.pop(0)
        print("13")
        
    elif num[3] == num[5] == player and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("14")
        
    elif num[6] == num[8] == player and (num[7] != "X" and num[7] != "O"):
        num[7] = x.pop(0)
        print("15")
        
    elif num[0] == num[8] == player and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("16")
        
    elif num[6] == num[2] == player and (num[4] != "X" and num[4] != "O"):
        num[4] = x.pop(0)
        print("17")
        
    elif num[0] == num[4] == player and (num[8] != "X" and num[8] != "O"):
        num[8] = x.pop(0)
        print("18")
        
    elif num[4] == num[8] == player and (num[0] != "X" and num[0] != "O"):
        num[0] = x.pop(0)
        print("19")
        
    elif num[6] == num[4] == player and (num[2] != "X" and num[2] != "O"):
        num[2] = x.pop(0)
        print("20")
        
    elif num[4] == num[2] == player and (num[6] != "X" and num[6] != "O"):
        num[6] = x.pop(0)
        print("21")
        
    elif (num[0] or num[2] or num[6] or num[8]) == player and len(x)==8:
        num[4] = x.pop(0)
        print("22")
        
    elif num[0]==num[8]==player or num[2]==num[6]==player and len(x)==6 and (num[1] != "X" and num[1] != "O"):
        num[1] = x.pop(0)
        print("23")
        
    elif len(x)==8 and num[4]==player:
        defend_random = random.choice(new_list)
        num[defend_random] = x.pop(0)
        print("45")
        
    elif len(x)==6 and num[abs(defend_random-8)] == player and num[4] == player:
        for i in (0,2,6,8):
            if num[i]!="X" and num[i]!="O":
                num[i]=x.pop(0)
                print("46")
                
                break
            else:
                pass
    #Defend code ends here
    #######################################################################

    else:
        while True:
            n = random.randint(0,8)
            if num[n] != "X" and num[n] != "O":
                num[n] = x.pop(0)
                print("Else")
                
                break
            else:
                pass
'''
The below segments will run every time to check the horizontal, vertical or diagonal matching
after the players and computers turn.
'''
      
def check():
    if num[0]==num[1]==num[2]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[3]==num[4]==num[5]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[6]==num[7]==num[8]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[0]==num[3]==num[6]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[1]==num[4]==num[7]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[2]==num[5]==num[8]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[0]==num[4]==num[8]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[2]==num[4]==num[6]==player:
        print(f"Player won the match")
        while len(x)!=0:
            x.pop()
    elif num[0]==num[1]==num[2]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[3]==num[4]==num[5]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[6]==num[7]==num[8]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[0]==num[3]==num[6]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[1]==num[4]==num[7]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[2]==num[5]==num[8]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[0]==num[4]==num[8]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    elif num[2]==num[4]==num[6]==computer:
        print(f"Computer won the match")
        while len(x)!=0:
            x.pop()
    else:
        pass

def player_turn():
    input_value = int(input("Enter the field"))
    clear_output()
    num[input_value-1] = x.pop(0)
    print_output()
    
  
def computer_first():
    from IPython.display import clear_output
    while True:
        if len(x) != 0:
            clear_output()
            computer_turn()
            print_output()
            if len(x) != 0:
                player_turn()
                clear_output()
                print_output()
            else:
                break
        else:
            break


def player_first():
    from IPython.display import clear_output
    while True:
        if len(x) != 0:
            clear_output()
            player_turn()
            print_output()
            if len(x) != 0:
                computer_turn()
                clear_output()
                print_output()
            else:
                break
        else:
            break


class Ask():
    def __init__(self):
        pass:
    def ask_again(self):
        play_again = input("Do you want to play again? Yes/No")
ask = Ask()

users_value = input("Do you want to toss a coin")

if users_value.lower() == "yes":
    user_toss = input("Enter 1 or 2")
    toss_list = [1,2]
    toss = random.choice(toss_list)
    if toss != user_toss:
        print("You lose the toss. Computer will make the first turn")
        x = [computer,player,computer,player,computer,player,computer,player,computer]
        computer_first()
    elif toss == user_toss:
        print("You won the toss. Make your first turn")
        x = [player,computer,player,computer,player,computer,player,computer,player]
        player_first()
elif users_value.lower() == "no":
    user_opinion = input("Do you want to play first. Yes/No")
    if user_opinion.lower()=="yes":
        x = [player,computer,player,computer,player,computer,player,computer,player]
        player_first()
    elif user_opinion.lower()=="no":
        print("Computer will make the first turn")
        x = [computer,player,computer,player,computer,player,computer,player,computer]
        computer_first()

def again_play():
    import random
    from IPython.display import clear_output
    player = "X"
    computer = "O"
    num = [" "]*9
    import random
    new_list = [0,2,6,8]
    if users_value.lower() == "yes":
        user_toss = input("Enter 1 or 2")
        toss_list = [1,2]
        toss = random.choice(toss_list)
        if toss != user_toss:
            print("You lose the toss. Computer will make the first turn")
            x = [computer,player,computer,player,computer,player,computer,player,computer]
            computer_first()
        elif toss == user_toss:
            print("You won the toss. Make your first turn")
            x = [player,computer,player,computer,player,computer,player,computer,player]
            player_first()
    elif users_value.lower() == "no":
        user_opinion = input("Do you want to play first. Yes/No")
        if user_opinion.lower()=="yes":
            x = [player,computer,player,computer,player,computer,player,computer,player]
            player_first()
        elif user_opinion.lower()=="no":
            print("Computer will make the first turn")
            x = [computer,player,computer,player,computer,player,computer,player,computer]
            computer_first()

    ask.ask_again()
ask.ask_again()
if ask.play_again.lower()=="yes":
    again_play()
else:
    pass
