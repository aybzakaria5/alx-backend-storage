#!/usr/bin/env python3
"""task 102"""


def top_students(mongo_collection):
    """task 101"""
    students = mongo_collection.find()

    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score

    sorted_students = sorted(students, key=lambda x: x['averageScore'],
                             reverse=True)
    return sorted_students
