import random 

#guess number should be between 1 and 100
guess_number = random.randint(1,100)

#enter a number between 1 and 100
print("Enter a numberr between 1 and 100")

#initialize the guess_count to 0
guess_count = 0

#initialize the guess to -1 
user_guess = -1

#while loop for guiding the user guesses
while user_guess != guess_number:
    user_guess = int(input("Please enter your number: "))

    if user_guess == guess_number:
        print("Yes!!!, you are correct, the number is", guess_number)
        guess_count += 1

    elif user_guess > guess_number:
        print("keep trying, the correct number is lower than your input")
        guess_count +=1

    else:
        print("Input a higher number")
        guess_count +=1

print("The number of times you guessed is: ", guess_count)
