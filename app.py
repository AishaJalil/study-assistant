from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
import markdown

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

# Core AI functions
def ask_question(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_text(text):
    prompt = f"Please summarize the following text:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def create_study_plan(topic, days):
    prompt = (
        f"Create a {days}-day study plan for learning the topic '{topic}'. "
        "Break it down into daily goals. Use clear formatting like bold headings for days and bullet points."
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    summary = ""
    plan = ""

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        text = request.form.get('text', '').strip()
        topic = request.form.get('topic', '').strip()
        days = request.form.get('days', '').strip()

        try:
            if question:
                raw_answer = ask_question(question)
                answer = markdown.markdown(raw_answer)
            if text:
                raw_summary = summarize_text(text)
                summary = markdown.markdown(raw_summary)
            if topic and days.isdigit():
                raw_plan = create_study_plan(topic, int(days))
                plan = markdown.markdown(raw_plan)
        except Exception as e:
            answer = f"Error: {str(e)}"

    return render_template("index.html", answer=answer, summary=summary, plan=plan)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
