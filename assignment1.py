university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

for student in university_data.values():
    print(f"{student['name']} - {student['major']}")

# output :

# Alice Johnson - Computer Science
# Bob Smith - Mathematics
# Clara Lopez - Physics

# -------------------------------------------------------------------------------------

for sid, student in university_data.items():
    print(f"{student['name']}:")
    for course, scores in student['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course} - Average: {avg:.2f}")
print()

# output:

# Alice Johnson:
#   Python101 - Average: 91.33
#   Math201 - Average: 81.00
# Bob Smith:
#   Math201 - Average: 90.33
#   Stats101 - Average: 83.00
# Clara Lopez:
#   Physics101 - Average: 78.33
#   Math201 - Average: 70.00

# ----------------------------------------------------------------------------------------------------------

for sid, student in university_data.items():
    python_course = student['courses'].get('Python101')
    if python_course and python_course.get('final', 0) > 90:
        print(f"  {student['name']} - Final: {python_course['final']}")
print()                                                                         #  Alice Johnson - Final: 92

university_data["S101"]["courses"]["AI101"] = {"midterm": 91, "final": 95, "project": 90}
print(university_data["S101"]["courses"]["AI101"])    #{'midterm': 91, 'final': 95, 'project': 90}

from collections import defaultdict

course_scores = defaultdict(list)

for student in university_data.values():
    for course, scores in student['courses'].items():
        avg_score = sum(scores.values()) / len(scores)
        course_scores[course].append(avg_score)

print("\nAverage score for each course:")
for course, scores in course_scores.items():
    overall_avg = sum(scores) / len(scores)
    print(f"{course}: {overall_avg:.2f}")

# output:

# Average score for each course:
# Python101: 91.33
# Math201: 80.44
# AI101: 92.00
# Stats101: 83.00
# Physics101: 78.33


