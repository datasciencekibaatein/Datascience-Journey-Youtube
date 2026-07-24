"""
grade_calculator.py — Grade calculation logic
"""

from config import PASSING_MARKS, GRADE_THRESHOLDS


def calculate_grade(percentage):
    for grade, threshold in GRADE_THRESHOLDS.items():
        if percentage >= threshold:
            return grade
    return "F"


def get_result_status(marks_dict):
    for marks in marks_dict.values():
        if marks < PASSING_MARKS:
            return "FAIL"
    return "PASS"


def calculate_percentage(marks_dict, max_per_subject=100):
    total = sum(marks_dict.values())
    percentage = round((total / (len(marks_dict) * max_per_subject)) * 100, 2)
    return total, percentage
