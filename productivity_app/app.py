from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Ensures proper session handling
notes=[]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculator", methods=["GET", "POST"])
def calculator_page():
    # For calculator
    result = ""
    if request.method == "POST" and "calc" in request.form:
        try:
            result = eval(request.form["calc"])
        except Exception as e:
            result = "Error"
    
    return render_template("calculator.html", result=result)

@app.route("/notes", methods=["GET", "POST"])
def notes_page():
    if request.method == "POST" and "note" in request.form:
        note = request.form["note"]
        notes.append(note)
    
    return render_template("notes.html", notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

