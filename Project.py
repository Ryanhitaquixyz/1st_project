# Make a stone paper seaser game

# 0:stone
# 1:paper
# 2:seasor:

def Game():

    import random

    comp=random.choice([0,1,2])



    You=input("Enter your choice \nst for stone,p for paper and sc for scissors:")

    Dict={"st":0,"p":1,"sc":2} # through this line of coad we define 0,1and 2 as "st","p","sc"

    reverseDict={0:"stone",1:"paper",2:"scissors"}# its helps to convert the numbers into words so that in print function it prints words instead of numbers

    You2=Dict[You] # this programe helps to convert [You]="st","p","sc" into [You2] numbers which is in the [Dict]

    print(f"You choose : {reverseDict[You2]}\n Computer choose :{reverseDict[comp]}")
                     # Here {reverseDict[You2] helps to covent You2 (which is number previously)into word}
    if(comp==You2):
       print("<>Its a Draw!<>")

    elif(comp==0 and You2==1):
       print("<>You Win!<>")
    elif(comp==1 and You2==0):
       print("<>Comp Win!<>")
    elif(comp==2 and You2==1):
          print("<>Comp Win!<>")
    elif(comp==1 and You2==2):
       print("<>You Win!<>")
    elif(comp==0 and You2==2):
       print("<>Comp Win!<>")
    elif(comp==2 and You2==0):
       print("<>You Win!<>")

    else:
       print("Something went wrong!")


Game()














# My first game is Here if i can buid this game I can do anything.


Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()
Game()


