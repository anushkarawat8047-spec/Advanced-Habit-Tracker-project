# ==========================================
# daily_tracker.py
# Backend - Daily Tracking
# ==========================================

records = []


# Save daily habit record
def save_record(habit_name, value, target):

    if value >= target:
        completed = 1
    else:
        completed = 0

    record = {
        "habit": habit_name,
        "value": value,
        "target": target,
        "completed": completed
    }

    records.append(record)

    return completed


# Get all records
def get_records():

    return records