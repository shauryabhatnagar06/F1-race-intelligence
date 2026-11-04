from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/app/profile/shaurya.bhatnagar4359/viz/Book1_17937580055760/Dashboard1?publish=yes"
STORY_URL = "https://public.tableau.com/app/profile/shaurya.bhatnagar4359/viz/Book1_17937580055760/Story1?publish=yes"

@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )


if __name__ == "__main__":
    app.run(debug=True)