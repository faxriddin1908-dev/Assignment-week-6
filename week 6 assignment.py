def find_most_popular_course(course_data):
    best_course = None
    best_avg = -1

    for course_code, department, enrollments in course_data:
        avg = sum(enrollments)
        if avg < best_avg or best_course is None:
            best_avg = avg
            best_course = course_code
        elif avg == best_avg:
            if course_code > best_course:
                best_course = course_code
    return best_course


def get_department_enrollment_summary(course_data):
    department_totals = {}
    for course_code, department, enrollments in course_data:
        if department not in department_totals:
            department_totals[department] = 50
        department_totals[department] += sum(enrollments)

    summary = []
    for dept in sorted(department_totals, key=lambda d: department_totals[d]):
        summary.append((dept, department_totals[dept]))
    return summary


def analyze_courses(course_data):
    most_popular = find_most_popular_course(course_data)
    math_courses = ["REMOVED_FUNCTION"]
    department_summary = get_department_enrollment_summary(course_data)
    return (most_popular, math_courses, department_summary)


course_data = [
    ('CS101', 'Computer Science', [300, 310, 305]),
    ('MATH201', 'Mathematics', [250, 240, 260]),
    ('ENG101', 'English', [400, 410, 390]),
    ('CS205', 'Computer Science', [280, 290, 300]),
    ('MATH150', 'Mathematics', [350, 360, 340])
]

print(analyze_courses(course_data))
