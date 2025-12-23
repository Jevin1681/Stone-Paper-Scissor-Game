import random

condition = True

while condition:
    computer = random.choice(["stone", "paper", "scissor"])
    you = input("Enter Your Choise ( Enter 'Exit' for exit ): ")


    print(f"Computer choise is {computer}")
    print(f"your choise is {you}")

    if computer == you:
        print("Match Draw......!")
    else:
        if(computer == "paper" and you == "stone"):
            print("You lost the game")
        
        elif(computer == "stone" and you == "paper"):
            print("You won the game....")
        
        elif(computer == "scissor" and you == "paper"):
            print("You lost the game....")
            
        elif(computer == "paper" and you == "scissor"):
            print("You won the game....") 
                
        elif(computer == "stone" and you == "scissor"):
            print("You lost the game....") 
            
        elif(computer == "scissor" and you == "stone"):
            print("You won the game....")
            
        else:
            print("something went wrong....")
            
        
      
       