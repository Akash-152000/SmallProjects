import random
def number():
    num = random.randrange(0,3)
    return num

while(True):
    try:
        guess = int(input("Enter your guess(between 0 to 20):"))
    except:
        print("Enter valid value.")
        
    if guess<0 or guess>20:
        print("Enter the value between range.")

    
    if number() == guess:
        print("********************Congratulations,you guessed it right*************")
        break
    else:
        print("Guess it again.")

