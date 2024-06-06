import random

print("----------Python mini project on 'Guessing the number'----------")
print("Try to guess the number between 1 to 100.")

gnrtd_num= random.randint(1,100)
attempts=0
guess=None

while gnrtd_num!=guess:
    guess=int(input("Guess the number: "))
    attempts+=1

    if guess>gnrtd_num:
        print("You guess too high! lower the number.")
    elif guess==0:
        print("guess between 1 to 100")
    elif guess<gnrtd_num:
        print("you guess too low! higher the number.")
    else:
        print(f"Congratulations! you guess the correct number in {attempts} attempts.")

