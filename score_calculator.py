def calculate_average_score(feedback_list):
    if not feedback_list:
        return 0
    total = sum(entry['score'] for entry in feedback_list)
    return total / len(feedback_list)
