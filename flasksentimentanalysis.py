from flask import Flask, request, render_template

from analysis import Analysis

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        keyword = request.form['keyword']

        a = Analysis(keyword)
        a.run()
        return f"Keyword: {keyword}, Subjectivity: {a.subjectivity}, Sentiment: {a.sentiment}"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()

