from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Example login credentials
        if username == "admin" and password == "password":
            message = "Login Successful!"
        else:
            message = "Invalid Username or Password."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)