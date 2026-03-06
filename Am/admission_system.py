# Student Admission Decision System

def get_cutoff(category):
    if category == "general":
        return 75
    elif category == "obc":
        return 65
    elif category == "sc_st":
        return 55
    else:
        return None


entrance_score = int(input("Entrance Score (0-100): "))
gpa = float(input("GPA (0-10): "))
recommendation = input("Recommendation letter (yes/no): ").lower()
category = input("Category (general/obc/sc_st): ").lower()
extra_score = int(input("Extracurricular score (0-10): "))


# Input validation
if not (0 <= entrance_score <= 100):
    print("Invalid entrance score")
    exit()

if not (0 <= gpa <= 10):
    print("Invalid GPA")
    exit()

if not (0 <= extra_score <= 10):
    print("Invalid extracurricular score")
    exit()


# Merit rule
if entrance_score >= 95:
    print("ADMITTED (Scholarship)")
    exit()


bonus = 0

if recommendation == "yes":
    bonus += 5

if extra_score > 8:
    bonus += 3


effective_score = entrance_score + bonus
cutoff = get_cutoff(category)


if cutoff is None:
    print("Invalid category")
    exit()


if gpa < 7:
    print("REJECTED: GPA below requirement")
elif effective_score >= cutoff:
    print("ADMITTED (Regular)")
elif effective_score >= cutoff - 5:
    print("WAITLISTED")
else:
    print("REJECTED")


print("Effective Score:", effective_score)