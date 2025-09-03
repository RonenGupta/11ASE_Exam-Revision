default_schedule = ["English", "Software", "Drama", "Science", "Sport"]
while True:
    day = input("Welcome to the timetable, what day do you want to view, or exit: ")
    if day.lower() == "monday":
        print("Monday")
        for index, period in enumerate(default_schedule):
            print(f"    Period {index + 1}: {period}")

    elif day.lower() == "tuesday":
        print("Tuesday")
        tuesday_schedule = default_schedule[:]
        last_day = tuesday_schedule.pop(len(tuesday_schedule) - 1)
        tuesday_schedule.insert(0, last_day)
        for index, period in enumerate(tuesday_schedule):
            print(f"    Period {index + 1}: {period}")

    elif day.lower() == "wednesday":
        print("Wednesday")
        wednesday_schedule = default_schedule[:]
        second_last_day = wednesday_schedule.pop(len(wednesday_schedule) - 2)
        last_day = wednesday_schedule.pop(len(wednesday_schedule) - 1)
        wednesday_schedule.insert(0, second_last_day)
        wednesday_schedule.insert(1, last_day)
        for index, period in enumerate(wednesday_schedule):
            print(f"    Period {index + 1}: {period}")

    elif day.lower() == "thursday":
        print("Thursday")
        thursday_schedule = default_schedule[:]
        third_last_day = thursday_schedule.pop(len(thursday_schedule) - 3)
        second_last_day = thursday_schedule.pop(len(thursday_schedule) - 2)
        last_day = thursday_schedule.pop(len(thursday_schedule) - 1)
        thursday_schedule.insert(0, third_last_day)
        thursday_schedule.insert(1, second_last_day)
        thursday_schedule.insert(2, last_day)
        for index, period in enumerate(thursday_schedule):
            print(f"    Period {index + 1}: {period}")

    elif day.lower() == "friday":
        print("Friday")
        friday_schedule = default_schedule[:]
        fourth_last_day = friday_schedule.pop(len(friday_schedule) - 4)
        third_last_day = friday_schedule.pop(len(friday_schedule) - 3)
        second_last_day = friday_schedule.pop(len(friday_schedule) - 2)
        last_day = friday_schedule.pop(len(friday_schedule) - 1)
        friday_schedule.insert(0, fourth_last_day)
        friday_schedule.insert(1, third_last_day)
        friday_schedule.insert(2, second_last_day)
        friday_schedule.insert(3, last_day)
        for index, period in enumerate(friday_schedule):
            print(f"    Period {index + 1}: {period}")

    elif day.lower() in ['exit', 'quit']:
        break
