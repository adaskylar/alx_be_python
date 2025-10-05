task = input("Enter your task")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "low":
        print(f"Note: {task} is a low priority task. Consider completing it when you have free time."
)
    case "medium":
        print(f"Note: {task} is a medium priority task. Consider completing it when you have free time.")

    case "high":
        if task == "high":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is not so high priority task. Consider completing it later.")