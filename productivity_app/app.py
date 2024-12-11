from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Ensures proper session handling
notes=[]

# Route for homepage with calculator and notes
@app.route("/", methods=["GET", "POST"])
def index():

    # For calculator
    result = ""
    if request.method == "POST" and "calc" in request.form:
        try:
            result = eval(request.form["calc"])
        except Exception as e:
            result = "Error"
    
    # For note-taking
    if request.method == "POST" and "note" in request.form:
        note = request.form["note"]
        notes.append(note)
    
    return render_template("index.html", result=result, notes=notes)

if __name__ == "__main__":
    app.run(debug=True)

