from collections import Counter

def summarize_feedback(feedback_list):
    top_scores = sorted(feedback_list, key=lambda x: x['score'], reverse=True)[:3]
    grade_count = Counter(entry['grade'] for entry in feedback_list)
    return {"top_scores": top_scores, "grade_count": dict(grade_count)}
