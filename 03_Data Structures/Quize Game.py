#This is the quize game made for kids using python 

quistions = ("Question 1: What is the largest planet in our solar system?",
             "Question 2: How many legs does a spider have?",
             "Question 3: What color do you get when you mix red and yellow?",
             "Question 4: Which animal is known as the King of the Jungle?",
             "Question 5: How many days are there in a week?")

options=(("A. EARTH", "B. JUPITER", "C. MARS", "D. SUN"),
         ("A. 6", "B. 8", "C. 10", "D. 4"),
         ("A. PURPLE", "B. GREEN", "C. ORANGE", "D. BROWN"),
         ("A. TIGER", "B. ELEPHANT", "C. LION", "D. BEAR"),
         ("A. 5", "B. 6", "C. 7", "D. 8"))

answers = ("B", "B", "C", "C", "C")
guesses = []
score = 0
question_num = 0

for question in quistions:
    print("----------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    print()
    guess = input("Enter the Correct option: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("You are Correct")
        score += 1
    else:
        print(f"Wrong!!, Correct answer is {answers[question_num]}. ")
    question_num += 1

print()
print("----------------------")
print("Correct Answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guessees: " ,end="")
for guess in guesses:
    print(guess, end=" ")
print()

result = (score/5)*100

print()
print("------- RESULT -------")
print(f"You have guess {score} answers right!!")
print(f"Your Final result is {result}")

print("----------------------")