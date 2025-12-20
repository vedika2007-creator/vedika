# AIIntervalAnalyzer.py
# Handles AI Interval Analysis logic

def analyze_intervals(student_data):
    """
    student_data: dict with keys 'name', 'skills', 'interests'
    Returns interval analysis as a dict
    """

    name = student_data.get("name", "Student")
    skills = student_data.get("skills", [])
    interests = student_data.get("interests", [])

    # --------------------------
    # Replace below logic with your real AI model later
    # Example simple calculation for now:
    interval_score = len(skills) * 10 + len(interests) * 5
    feedback = "Excellent" if interval_score > 20 else "Good"
    # --------------------------

    return {"name": name, "interval_score": interval_score, "feedback": feedback}