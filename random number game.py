import random

def game(n):
    if n==1:
        print("You have choosen easy difficulty")
        print(" ")
        print("You will have 10 chances to guess the right number")
        print(" ")
        print("BEST OF LUCK!")

        x=random.randrange(1,100)


        COUNT=0
        print("A random number has been generated")
        
        while COUNT < 10:
            y=int(input("Guess the number: "))
            COUNT+=1
            if x!=y:
                if y>x:
                    print("The random number is less than",y)  
                else:
                    print("The random number is greater than",y)
            if x==y:
                print("Hurray! You have guessed the right number in",COUNT,"attempts")
                return
        
        print("Game over, the correct number was:",x)
                
    if n==2:
        
        print("You have choosen medium difficulty")
        print(" ")
        print("You will have 5 chances to guess the right number")
        print(" ")
        print("BEST OF LUCK!")

        x=random.randrange(1,100)


        COUNT=0
        print("A random number has been generated")
        
        while COUNT < 5:
            y=int(input("Guess the number: "))
            COUNT+=1
            if x!=y:
                if y>x:
                    print("The random number is less than",y)  
                else:
                    print("The random number is greater than",y)
            if x==y:
                print("Hurray! You have guessed the right number in",COUNT,"attempts")
                return
        
        print("Game over, the correct number was:",x)
    
    if n==3:
        print("You have choosen easy difficulty")
        print(" ")
        print("You will have 3 chances to guess the right number")
        print(" ")
        print("BEST OF LUCK!")

        x=random.randrange(1,100)


        COUNT=0
        print("A random number has been generated")
        
        while COUNT < 3:
            y=int(input("Guess the number: "))
            COUNT+=1
            if x!=y:
                if y>x:
                    print("The random number is less than",y)  
                else:
                    print("The random number is greater than",y)
            if x==y:
                print("Hurray! You have guessed the right number in",COUNT,"attempts")
                return
        
        print("Game over, the correct number was:",x)


def main():
    print("Welcome to this number guessing game")
    print(" ")
    print("You need to guess a number between 1-100 in chances to win the game")
    print(" ")
    print("Choose any difficulty from the options given below:")
    print(" ")

    print("1. Easy Difficulty(10 chances)")
    print("2. Medium difficulty Difficulty(5 chances)")
    print("3. Hard Difficulty(3 chances)")

    inp=int(input("Choose your difficulty(use number to choose difficulty): "))
    game(inp)

    
main()


