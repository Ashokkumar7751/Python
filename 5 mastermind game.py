import random

# Generate a random 4-digit number
num = random.randrange(1000, 10000)
print(num)

n = int(input("Guess the 4-digit number: "))

# Check if the user guessed correctly on the first try
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 1  # Start count from 1 since the first guess has already been made
    num_str = str(num)  # Convert the random number to a string once

    while n != num:
        count = 0
        n_str = str(n)  # Convert the user input to a string

        # List to store correctly guessed digits
        correct = ['X'] * 4

        # Check which digits are correct
        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        # Provide feedback to the user
        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
        else:
            print("None of the numbers in your input match.")

        print("\n")

        # Get the next guess from the user
        n = int(input("Enter your next choice of numbers: "))
        ctr += 1  # Increment attempt counter

    # When the user guesses the correct number
    print("You've become a Mastermind!")
    print(f"It took you only {ctr} tries.")
