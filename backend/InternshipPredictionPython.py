# InternshipPredictionPython.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend on another port (Live Server 5500) to talk to this backend

# Define internships with required skills and possible companies
internship_options = {
    "AI": {
        "title": "AI Intern",
        "required_skills": ["Python", "Machine Learning", "Data Structures"],
        "places": ["Google", "Microsoft", "DeepMind"]
    },
    "Web Development": {
        "title": "Web Developer Intern",
        "required_skills": ["HTML", "CSS", "JavaScript"],
        "places": ["TCS", "Infosys", "Zoho", "Wipro"]
    },
    "Cybersecurity": {
        "title": "Cybersecurity Intern",
        "required_skills": ["Networking", "Python", "Ethical Hacking"],
        "places": ["Cisco", "IBM", "Paladion"]
    },
    "Data Science": {
        "title": "Data Science Intern",
        "required_skills": ["Python", "Pandas", "Statistics"],
        "places": ["Amazon", "TCS", "Accenture"]
    }
}

@app.route("/predict", methods=["POST"])
def predict_internship():
    data = request.get_json()
    name = data.get("name", "Student")
    skills = [s.strip() for s in data.get("skills", [])]
    interests = data.get("interests", [])
    cgpa = float(data.get("cgpa", 0))
    courses = [c.strip() for c in data.get("courses", [])]

    # Default values
    best_fit = "No clear match"
    place = "N/A"
    strengths = []
    weaknesses = []
    areas = []

    if interests:
        interest = interests[0]
        if interest in internship_options:
            required_skills = internship_options[interest]["required_skills"]
            matched_skills = [skill for skill in skills if skill in required_skills]

            # Determine best fit based on matched skills
            if len(matched_skills) >= 2:
                best_fit = internship_options[interest]["title"]
            else:
                best_fit = f"{internship_options[interest]['title']} (Skill improvement recommended)"

            # Pick the first place for now
            place = internship_options[interest]["places"][0]

            # Strengths & Areas
            for req_skill in required_skills:
                if req_skill in skills:
                    strengths.append(f"Knowledge in {req_skill}")
                else:
                    areas.append(f"Learn {req_skill}")

    # CGPA evaluation
    if cgpa >= 8:
        strengths.append("Strong academic performance")
    else:
        weaknesses.append("Improve academic score")

    # Courses evaluation
    for course in courses:
        if course not in skills and course not in strengths:
            areas.append(f"Course studied but skill not applied: {course}")

    return jsonify({
        "best_fit": best_fit,
        "place": place,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "areas": areas
    })


if __name__ == "__main__":
    app.run(debug=True)