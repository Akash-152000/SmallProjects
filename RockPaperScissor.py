import random
RPS=["ROCk","PAPER","SCISSOR"]
user=0
computer=0
print("If u want to exit type exit")
print("If u want to see score press score")
while True:
    enter = input("Enter:")
    enter = enter.upper()
    random_rps = random.choice(RPS)
    if enter==random_rps:
        print(random_rps)
        print("draw")
    elif enter=="ROCK" and random_rps=="PAPER":
        print(random_rps)
        computer+=1
    elif enter=="ROCK" and random_rps=="SCISSOR":
        print(random_rps)
        user+=1
    elif enter=="PAPER" and random_rps=="SCISSOR":
        print(random_rps)
        computer+=1
    elif enter=="PAPER" and random_rps=="ROCK":
        print(random_rps)
        user+=1
    elif enter=="SCISSOR" and random_rps=="ROCK":
        print(random_rps)
        computer+=1
    elif enter=="SCISSOR" and random_rps=="PAPER":
        print(random_rps)
        user+=1
    elif enter=="EXIT":
        break
    elif enter=="SCORE":
        print("Computer:",computer)
        print("User:",user)
    else:
        print("Enter valid value")

print("Computer:",computer)
print("User:",user)
if computer>user:
    print("you lose")
elif computer==user:
    print("Draw")
else:
    print("************************************")
    print("************************************")
    print("************************************")
    print("************************************")
    print("***************YOU WIN**************")
    print("************************************")
    print("************************************")
    print("************************************")
    
