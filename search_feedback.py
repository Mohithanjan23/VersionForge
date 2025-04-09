def search_feedback(feedback_list, student_name):
    return [entry for entry in feedback_list if entry['name'].lower() == student_name.lower()]
  
