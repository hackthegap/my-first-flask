from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        amount = float(request.form.get("amount"))
        result = amount * 1.1  # just an example (like +10%)
        return render_template("result.html", name=name, result=result)
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # You can extract and print or process registration data here
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"Registered: {full_name}, {email}")
        return "Registration submitted!"  # Simple response
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
