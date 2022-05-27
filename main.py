import random 
number = random.randint(1,10)

player_name= input("Hello, What's your name ?")
number_of_guesses = 0
print('Okay ' + player_name + ' I am guessing a number between 1 and 10 : ')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print("Your Guess Is Too Low")
    if guess == number:
        break
while number_of_guesses >= 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print("Your Guess Is Too High")
    if guess == number:
        break

if guess == number: 
    print("You Guessed The Number in " + str(number_of_guesses)+ " Tries!")
else: 
    print("You Did Not Guess The Number,The Number Was" + str(number))