
skills = {"python": 3, "numpy": 1, "pandas": 1, "linear algebra": 2}

skills_to_improve = [skill for skill in skills if skills[skill]<3]
print(skills_to_improve)


with open("notes.txt", 'r') as file:
    lines = sum(1 for _ in file)
        
print(f"your file has {lines} lines")

def update_skill(skills_dict, skill_name, new_level):
    try:
        if(1 < new_level < 5):
            skills_dict[skill_name] = new_level
        else:
            raise ValueError("skill level should be between 1 and 5")
    except ValueError as v:
        print(f"ERROR: {v}")
    except Exception as e:
        print(f"ERROR: {e}")


try:
    update_skill(skills, "python", 4)
    update_skill(skills, "numpy", 5)
except ValueError as e:
    print(f"ERROR: {e}")