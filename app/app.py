from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("mainpage.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8888)