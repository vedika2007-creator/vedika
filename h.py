# Example pseudocode
internships = [
    {"name": "Google STEP", "domain": "AI", "location": "USA"},
    {"name": "Microsoft Explore", "domain": "Web Dev", "location": "USA"},
    {"name": "ISRO Summer", "domain": "Robotics", "location": "India"},
]

def calculate_fit(student_choices):
    best_score = -1
    best_internship = None
    for internship in internships:
        score = 0
        if internship["domain"] == student_choices["domain"]:
            score += 5
        if internship["location"] == student_choices["location"]:
            score += 3
        if internship.get("skills") and any(skill in student_choices["skills"] for skill in internship["skills"]):
            score += 2
        if score > best_score:
            best_score = score
            best_internship = internship["name"]
    return best_internship

student_choices = {"domain": "AI", "location": "USA", "skills": ["Python", "ML"]}
best_fit = calculate_fit(student_choices)
print(best_fit)