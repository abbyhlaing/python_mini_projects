questions = [
    [1, "England", "London"],
    [2, "France", "Paris"],
    [3, "Spain", "Madrid"],
    [4, "Italy", "Rome"],
    [5, "Germany", "Berlin"],
    [6, "Scotland", "Edinburgh"],
    [7, "Wales", "Cardiff"],
    [8, "United Arab Emirates", "Abu Dhabi"],
    [9, "China", "Beijing"],
]

print("Menu: \n[1] Add player name \n[2] Play guess the capital city \n[3] End game\n")
a = int(input("Enter your menu choice (1 to 3): "))

if a == 1:
    b = str(input("Enter the player name: "))
    print("The player name is:", b)
    print("Menu: \n[1] Add player name \n[2] Play guess the capital city \n[3] End game\n")
    a = int(input("Enter your menu choice (1 to 3): "))

if a == 2:
    selected_questions = set()
    score = 0
    for i in range(5):
        while True:
            q = int(input("Enter your chosen number for question (1 to 9), but don't choose the same question twice: "))
            if q not in selected_questions:
                selected_questions.add(q)
                break
            else:
                print("You have already chosen that question. Please choose a different one.")
        print(f"What is the capital city of {questions[q-1][1]}?")
        c = str(input("Enter the answer: "))
        if c.lower() == questions[q-1][2].lower():
            print("Congratulations! You're right.")
            score += 1
        else:
            print(f"Sorry! For this question, you're wrong.") 
    print("Your score:", score)
    print("Menu: \n[1] Add player name \n[2] Play guess the capital city \n[3] End game\n")
    a = int(input("Enter your menu choice (1 to 3): "))

if a == 3:
    confirm = input("Are you sure you want to end the game? (yes/no): ")
    if confirm.lower() == "yes":
        print("End the game.")
        
    else:
        print("Menu: \n[1] Add player name \n[2] Play guess the capital city \n[3] End game\n")
        a = int(input("Enter your menu choice (1 to 3): "))
    