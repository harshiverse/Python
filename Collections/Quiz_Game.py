#PYTHON QUIZ GAME
## This is a simple quiz game that tests the user's knowledge on various topics. The game will ask a series of questions and keep track of the user's score. At the end of the game, it will display the user's final score.
### Fundamental concepts used: Collections, Functions, Loops, Conditionals

questions = ("What is the capital of India?",
             "What is the largest mammal?", 
             "What is the chemical symbol for water?", 
             "What is the largest planet?", 
             "What is the smallest prime number?")

options = (("a) Mumbai", "b) New Delhi", "c) Kolkata", "d) Chennai"),
           ("a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Hippopotamus"),
           ("a) H2O", "b) CO2", "c) O2", "d) NaCl"),
           ("a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"),
           ("a) 0", "b) 1", "c) 2", "d) 3"))    

answers = ("b", "b", "a", "c", "c")
guesses = []  # Initialize an empty list to store the user's guesses
score = 0  # Initialize score to 0
question_num = 0  # Initialize question number to 0

for question in questions:
    print("----------------")
    print(question)  # Print the current question
    for option in options[question_num]:
        print(option)  # Print the options for the current question

    guess = input("Enter your answer (a, b, c, or d): ")  # Get the user's guess
    guesses.append(guess)  # Add the user's guess to the list of guesses
    if guess == answers[question_num]:  # Check if the user's guess is correct
        score += 1  # Increment the score if the guess is correct
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is: {answers[question_num]}")  # Print the correct answer if the user's guess is wrong
    question_num += 1  # Increment the question number

print("Quiz Completed!")
print("\n---------------------")
print("       RESULTS       ")
print("---------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")  # Print the correct answers
print()  # Print a newline

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")  # Print the user's guesses
    print(answer, end=" ")  # Print the correct answer for each question
print()  # Print a newline

score = int(score / len(questions) * 100)  # Calculate the final score as a percentage
print(f"Your final score is: {score}%")  # Print the final score
