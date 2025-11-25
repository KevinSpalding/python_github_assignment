print("Welcome to my Python program!") #Welcome message 
hours = input("How many hours did you study today? ") #Hours studied input
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} hours this week.")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.") #Basic error handling
    exit()
