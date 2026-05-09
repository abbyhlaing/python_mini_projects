import random

words = ["antelope", "ape", "badger", "bear", "beaver", "bison", "crocodile", "elephant",
         "elk", "ferret", "goat", "goose", "kangaroo", "llama", "lion", "monkey", "moose",
         "orangutan", "shark", "snake", "tiger", "whale", "wombat"]


secret_word = random.choice(words)
print(secret_word)

print("Welcome to Guess the Animal Game!")
print(f"The secret word has {len(secret_word)} letters.")

a=3
for i in range (0,len(secret_word)+a):
    print("\nAttempt left: ",(len(secret_word)+a)-i)
    word = str(input(F"Enter a word with {len(secret_word)} letters: "))
    
            
    if word == secret_word:
        print("Congratulations! You guessed the secret word.")
        break
    elif len(word)!=len(secret_word):
        print("Please enter a word with the correct length.")
        a += 1


    else:
        correct_letters = set()
        wrong_letters = set()
        for i in word:
            if i in secret_word:
                correct_letters.add(i)
                
            else:
                wrong_letters.add(i)
                
        print(f"Incorrect guess. Try again. \nCorrect letters: {correct_letters} \nWrong letters: {wrong_letters}")



