# Challenge: Student Grade Manager
"""
Inputs:

{
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 80],
    "Charlie": [95, 92, 93]
}

Out put:

Averages:
Alice: 87.67
Bob: 75.00
Charlie: 93.33

Top student: Charlie
"""

students = {"Alice": [85, 90, 88], "Bob": [70, 75, 80], "Charlie": [95, 92, 93]}

def calculate_average(scores: dict):

    averages = {}

    for name, score in scores.items():
        averages[name] = float(f"{sum(score) / len(score):.2f}")

    find_top_student(averages)


def find_top_student(data: dict):
    top_student = None
    highest_score = 0

    print("Averages:")

    for name, score in data.items():

        print(f"{name}: {score}")

        if score > highest_score:
            highest_score = score
            top_student = name

    print(f"\nTop student: {top_student}")




print(calculate_average(students))

############################## REFACTOR ##############################

""" 
The core idea

A function should:

Do one thing
Do it well
Not mix responsibilities
"""

students = {"Alice": [85, 90, 88], "Bob": [70, 75, 80], "Charlie": [95, 92, 93]}


# this function focus only in one thing is to calculate the average of each students
def calculate_average(students: dict) -> dict:

    averages = {}
    for name, average in students.items():
        total_average = sum(average) / len(average)
        averages[name] = round(total_average, 2)

    return averages

# this function determines who is the highest_average students
def find_top_student(averages: dict) -> str:
    top_student = None
    highest_average = 0

    for name, average in averages.items():
        if average > highest_average:
            highest_average = average
            top_student = name

    return f"\nTop student: {top_student}"


def print_me():
    averages = calculate_average(students)
    top_student = find_top_student(averages)

    print("Averages:")
    for name, average in averages.items():
        print(f"{name}: {average}")

    print(top_student)


print_me()

