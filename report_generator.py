def generate_report(feedback_list, filename="feedback_report.txt"):
    with open(filename, 'w') as f:
        for entry in feedback_list:
            f.write(f"Name: {entry['name']}, Grade: {entry['grade']}, Score: {entry['score']}, Comment: {entry['comment']}\n")
