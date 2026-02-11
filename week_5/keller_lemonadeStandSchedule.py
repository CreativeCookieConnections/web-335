"""
Author: Aisha Keller
Date: 2/11/2026
File Name: keller_lemonadeStandSchedule.py
Description: Print lemonade stand tasks and a weekly schedule.
"""

# List of at least five tasks related to running a lemonade stand
tasks = [
    "Buy supplies",
    "Squeeze lemons",
    "Add sugar",
    "Pour water",
    "Stir mixture",
    "Fill containers",
    "Serve customers",
    "Count earnings",
    "Clean up",
]

# Use a for loop to iterate over the list of tasks and print them
for task in tasks:
    print(task)

# Create a list of days (Sunday through Saturday)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Iterate over days and show the schedule with an if...else statement
weekday_task_index = 0
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(day + ": Day off, rest")
    else:
        print(day + ": " + tasks[weekday_task_index])
        weekday_task_index += 1

    

