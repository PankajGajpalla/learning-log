from datetime import datetime

goal = [ "fine-tune a model", "high income", "get a job at google"]

for i,a in enumerate(goal):
    print(f"{i+1}. {a}")

def years_remaining(target_year:int):
    return f"years left: {target_year - datetime.now().year}"

print(years_remaining(2030))