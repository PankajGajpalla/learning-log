from datetime import datetime

goals = [ "fine-tune a model", "high income", "get a job at google"]

for i,goal in enumerate(goals):
    print(f"{i+1}. {goal}")

def years_remaining(target_year:int) -> int:
    return target_year - datetime.now().year

print(f"years left: {years_remaining(2030)}")