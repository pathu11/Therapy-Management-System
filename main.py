from flask import Flask , redirect ,url_for,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/test/<id>")
def test(id):
    return f"hello test {id}"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/auth")
def auth():
    return redirect(url_for("user",name="Publisher"))

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__  == "__main__":
    app.run()