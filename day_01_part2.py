
skills = {"python": 3, "numpy": 1, "pandas": 1, "linear algebra": 2}

skills_to_improve = [skill for skill in skills if skills[skill]<3]
print(skills_to_improve)


with open("notes.txt", 'r') as file:
    lines = sum(1 for _ in file)
        
print(f"your file has {lines} lines")

def update_skill(skills_dict, skill_name, new_level):
    if not (1 <= new_level <= 5):
        raise ValueError(f"new_level must be between 1 and 5, got {new_level}")
    skills_dict[skill_name] = new_level
    return skills_dict

print("\n--- Testing update_skill ---")
print(f"Before: {skills}")

update_skill(skills, "python", 5)
print(f"After valid update (python=5): {skills}")

try:
    update_skill(skills, "numpy", 10)
except ValueError as e:
    print(f"Caught expected error: {e}")

for level in [1, 5]:
    try:
        update_skill(skills, "test_skill", level)
        print(f"Level {level} accepted ✓")
    except ValueError as e:
        print(f"Level {level} rejected: {e}")

print(f"\nWeak skills (below 3): {skills_to_improve}")