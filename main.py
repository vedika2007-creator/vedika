import os
from flask import Flask, render_template, request
import csv

# Import your backend scripts
from backend import AIIntervalAnalyzer 
from backend import gemini_ai
from backend import InternshipPredictionPython 

app = Flask(__name__)

# ---------- FRONTEND ROUTES ----------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/prep')
def prep():
    return render_template('prep.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/rating')
def rating():
    return render_template('rating.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

# ---------- FEEDBACK ROUTE ----------

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        name = request.form['name']
        comment = request.form['comment']

        # Save feedback in feedback.csv
        with open('feedback.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, comment])

        return "Thank you for your feedback!"
    except Exception as e:
        return f"Error saving feedback: {e}"

# ---------- AI / BACKEND ROUTES (example) ----------
# You can create routes to call your backend scripts if needed

@app.route('/run_ai', methods=['POST'])
def run_ai():
    # Example of calling AI functions
    # data = request.form['data']
    # result = ai_interval_analyzer.process(data)
    # return result
    return "AI function route ready!"


# ---------- MAIN ----------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Dynamic port for deployment

    app.run(host='0.0.0.0', port=port)
