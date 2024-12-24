from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded username and password for demonstration
USERNAME = "admin"
PASSWORD = "password"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username == USERNAME and password == PASSWORD:
            return "Login Successful!"
        else:
            error = "Invalid Credentials. Please try again."
    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
