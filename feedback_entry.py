def collect_feedback():
    feedback_list = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        grade = input("Enter grade (A/B/C/D/F): ")
        try:
            score = float(input("Enter score (0-100): "))
        except ValueError:
            print("Invalid score. Try again.")
            continue
        comment = input("Enter feedback comment: ")
        feedback = {"name": name, "grade": grade.upper(), "score": score, "comment": comment}
        feedback_list.append(feedback)
    return feedback_list
