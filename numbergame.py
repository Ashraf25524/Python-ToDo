right_number = 23
guessing_times = 3
guessed_times = 0
while guessed_times <= guessing_times:
    guessed_number = int(input("Guess a number between 0 and 50: > "))
    if guessed_number == right_number:
        print("You guessed the right number")
        break
    else:
        guessed_times = guessed_times + 1
        print("Wrong number. Try again")
else:
    print("You have exhausted your guessed times")