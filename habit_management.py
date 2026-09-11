# ==========================================
# habit_management.py
# Backend - Habit Management
# ==========================================

habits = []


# Add a new habit
def add_habit(name, target):

    habit = {
        "name": name,
        "target": target
    }

    habits.append(habit)

    return True


# Get all habits
def get_habits():

    return habits


# Delete a habit
def delete_habit(name):

    for habit in habits:

        if habit["name"].lower() == name.lower():

            habits.remove(habit)

            return True

    return False