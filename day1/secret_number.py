

secret_number = int(input("Enter the secret number: "))

for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3 - Guess the number: "))

    if guess == secret_number:
        print(f"\n*** CORRECT! The secret number is {secret_number} ***")
        break
    else:
        print("Wrong guess!")

else:
    print(f"\nYou have used all 3 attempts. The secret number was {secret_number}.")