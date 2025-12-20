# Gemini.aipy
# Backend for WebsterAI
# Integrates Internship Prediction and AI Interval Analyzer
# Exposes Flask API endpoints for frontend

# Step 1: Import required libraries
from flask import Flask, request, jsonify

# Step 2: Import your AI scripts
# Make sure the files are in the same backend folder
from InternshipPredictionPython import predict_internship
from AIIntervalAnalyzer import analyze_intervals

# Step 3: Create Flask app
app = Flask(__name__)

# -----------------------------
# Step 4: Backend Functions
# -----------------------------

def predict_internship_backend(student_data):
    """
    Calls your InternshipPredictionPython.py logic
    student_data: dict from frontend
    Returns: dict with prediction result
    """
    result = predict_internship(student_data)
    return result

def analyze_intervals_backend(student_data):
    """
    Calls your AIIntervalAnalyzer.py logic
    student_data: dict from frontend
    Returns: dict with analysis result
    """
    result = analyze_intervals(student_data)
    return result

# -----------------------------
# Step 5: Flask API Routes
# -----------------------------

# Route for Internship Prediction
@app.route('/predict', methods=['POST'])
def predict():
    student_data = request.json  # Receive JSON from frontend
    result = predict_internship_backend(student_data)
    return jsonify(result)

# Route for AI Interval Analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    student_data = request.json
    result = analyze_intervals_backend(student_data)
    return jsonify(result)

# -----------------------------
# API route for internship prediction
@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.json
    skills = data.get("skills", "")
    interest = data.get("interest", "")
    result = predict_internship(skills, interest)
    return jsonify({"prediction": result})

# API route for interview analysis
@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.json
    answer = data.get("answer", "")
    result = analyze_interval(answer)
    return jsonify({"analysis": result})
# Step 6: Run the Flask Server
# -----------------------------
if __name__ == "__main__":
    print("Starting GeminiAI Backend Server on http://127.0.0.1:5000")

    app.run(host='0.0.0.0', port=5000)
