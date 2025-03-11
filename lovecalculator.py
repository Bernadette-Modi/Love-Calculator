from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def love_calculator():
    if request.method == "POST":
        name1 = request.form["name1"]
        name2 = request.form["name2"]

        love_score = random.randint(50, 100)

        if love_score > 85:
            message = "You two are a match made in heaven! ❤️"
        elif love_score > 70:
            message = "You have great chemistry! 💞"
        else:
            message = "There's potential! Keep the love growing! 💖"
        return render_template("index.html", name1=name2, name2=name2, love_score=love_score, message=message)
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)