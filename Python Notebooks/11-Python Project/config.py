"""
config.py — Constants for Student Marks Management System
Change values here; they reflect everywhere automatically.
"""

CSV_FILE = "students.csv"
JSON_FILE = "students_report.json"

SUBJECTS = ["Physics", "Chemistry", "Maths", "English", "Computer"]

MAX_MARKS = 100
MIN_MARKS = 0
PASSING_MARKS = 33

GRADE_THRESHOLDS = {
    "A+": 90,
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50,
    "E": 33,
    # Below 33 → F
}


