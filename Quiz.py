#Ask question and collect response from userprint
#check if the user response is equal to 'answer' print correct
#else print incorrect
#sum up the number of questions answered correctly


questions = [
    {
        "question": "Which country has the largest Economy in Africa? ", 
        "answer": "Nigeria"
    },
    {
        "question": "What month is Nigeria's independence? ", 
        "answer": "October"
    },
    {
        "question": "What is the name of the Nigeria currency? ", 
        "answer": "Naira"
    }
]

point = 0

for question in questions:
    user_response = input(question["question"] + ": ")
    if user_response.lower() == question["answer"].lower():
        print("That's Correct!...Welldone")
        point += 1
    else:
        print("Oops... That's Incorrect!. The correct answer is " + question["answer"] + ".")

print("Your final score is " + str(point) + " out of " + str(len(questions)) + ".")
