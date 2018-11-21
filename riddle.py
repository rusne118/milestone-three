import os

guess = 0 

while True:
    print ("The more you take, the more you leave behind. What am I?")
    print ("Stuck? Type HINT for some help or GIVE UP to reveal the answer")
    answer = input ()
    guess += 1
    
    if "Footsteps" in answer :
        print ("Correct!")
        print ("It took you" + str(guess)+ "guesses")
        break
    
    elif answer.upper()  == "HINT":
        print ("We leave them behind")
        
    elif answer.upper() == "GIVE UP":
        print ("The correct answe was Footsteps")
        break
    else: 
        print ("Try Again!")
        