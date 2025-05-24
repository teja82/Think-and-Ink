from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/writing_styles")
def writing_styles():
    return render_template("redirect.html")

@app.route("/about_us")
def about_us():
    return render_template("aboutus.html")

@app.route("/feedback_")
def feedback():
    return render_template("feedback.html")

@app.route("/start_blog")
def start_blog():
    subprocess.Popen(["streamlit", "run", "backend/blog.py", "--server.port=8501"])
    return "Blog app started on port 8501"

@app.route("/start_debate")
def start_debate():
    subprocess.Popen(["streamlit", "run", "backend/debate.py", "--server.port=8502"])
    return "Debate app started on port 8502"

@app.route("/start_story")
def start_story():
    subprocess.Popen(["streamlit", "run", "backend/story.py", "--server.port=8503"])
    return "Story app started on port 8503"

# ✅ Correct Render-compatible run block
if __name__ == "__main__":
    app.run(debug=True)