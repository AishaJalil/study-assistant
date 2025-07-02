import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyBwFia6DHVl-9Qcy2tqPymXzhxQtm4PqSA") 

model = genai.GenerativeModel("gemini-1.5-flash")

# Function: Ask a question
def ask_question(question: str) -> str:
    prompt = f"Answer this student question clearly and briefly:\n\n{question}"
    response = model.generate_content([prompt])
    return response.text.strip()

# Function: Summarize given text
def summarize_text(text: str) -> str:
    prompt = f"Summarize the following content in simple terms for a student:\n\n{text}"
    response = model.generate_content([prompt])
    return response.text.strip()

# Function: Create a study plan
def create_study_plan(subject, days):
    prompt = f"Create a {days}-day study plan to master {subject}. Return the plan in HTML list format."
    response = model.generate_content(prompt)
    return response.text
