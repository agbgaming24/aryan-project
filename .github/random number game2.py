#------making function guess
def guess():

#------setting lower and higher values and choice to 0
    low=1
    maxi=100
    choice=0

    #------intro screen with rules


    print("Welcome to number guessing game")
    print("")
    print("Before starting, the game has following rules:")
    print(" ")
    print("1. The computer will guess the number of times the user want it to")
    print("")
    print("2. When the computer guesses a number, you will have 3 options to choose from(L,H,C)")
    print("")
    print("  lower(l):Use this if the computer value is lower than the guessed value")
    print("  higher(h):Use this if the computer value is higher than the guessed value")
    print("  correct(l):Use this if the computer guesses the value")
    print(" ")
    print("3. Provide answers from the options provided only")
    print("")
    print("Hope you enjoy the game :)")

#------providing options to user for number of guesses

    print("10 chances(1)")
    print("5 chances(2)")
    print("3 chances(3)")
#------using try-except exception method
    try:
        #------asking for user input
        n=int(input("Select number of choices: "))
    #------guessing system
        if n==1:
            while choice<10:
                mid=(low+maxi)//2
                print("My guess is",mid)
                choice+=1
                x=input("is my guess correct?(L,H,C): ").lower()
                if x=="l":
                    low=mid+1
                    
                elif x=="h":
                    maxi=mid-1
                elif x=="c":
                    print("Number guessed!")
                    print("I guessed it in",choice,"attempts!")
                    return
                else:
                    print("Wrong input")

            print("Game over, I lost")
        
        if n==2:
            while choice<5:
                mid=(low+maxi)//2
                print("My guess is",mid)
                choice+=1
                x=input("is my guess correct?(L,H,C): ").lower()
                if x=="l":
                    low=mid+1
                    
                elif x=="h":
                    maxi=mid-1
                elif x=="c":
                    print("Number guessed!")
                    print("I guessed it in",choice,"attempts!")
                    return
                else:
                    print("Wrong input")
                
            print("Game over, I lost")

        if n==3:
            while choice<3:
                mid=(low+maxi)//2
                print("My guess is",mid)
                choice+=1
                x=input("is my guess correct?(L,H,C): ").lower()
                if x=="l":
                    low=mid+1
                    
                elif x=="h":
                    maxi=mid-1
                elif x=="c":
                    print("Number guessed!")
                    print("I guessed it in",choice,"attempts!")
                    return
                else:
                    print("Wrong input")
                
            print("Game over, I lost")

                    
    except:
        #------using the following if the computer encounters any exception
        print("Invalid input")
        print(" ")
        return guess()

    
guess()