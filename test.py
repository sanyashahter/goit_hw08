from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays_per_week = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].replace(year=today.year).date()

        if start_of_week <= birthday <= end_of_week:
            weekday = weekdays[birthday.weekday()]
            birthdays_per_week[weekday].append(name)

    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")


users = [
    {"name": "Bill", "birthday": datetime(1990, 6, 19)},
    {"name": "Jill", "birthday": datetime(1985, 6, 20)},
    {"name": "Kim", "birthday": datetime(1978, 6, 23)},
    {"name": "Jan", "birthday": datetime(1992, 6, 23)},
    {"name": "Alex", "birthday": datetime(1989, 6, 26)},
]

get_birthdays_per_week(users)
