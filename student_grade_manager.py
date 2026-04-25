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


def calculate_average(scores: dict):

    averages = {}

    for name, score in scores.items():
        averages[name] = float(f"{sum(score) / len(score):.2f}")

    return averages


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


students = {"X": [60, 70, 80]}

print(calculate_average(students))
