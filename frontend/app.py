from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_BASE_URL = os.getenv("API_BASE_URL")

@app.route("/", methods=["GET", "POST"])
def home():
    prayers = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        country = request.form.get("country")

        try:
            response = requests.get(
                f"{API_BASE_URL}/prayer-times",
                params={"city": city, "country": country},
                timeout=10
            )
            response.raise_for_status()
            prayers = response.json()["data"]["timings"]

        except Exception:
            error = "Unable to fetch prayer times. Please try again."

    return render_template("index.html", prayers=prayers, error=error)

if __name__ == "__main__":
    app.run(debug=True)
