from flask import Flask, request, jsonify, render_template
from tasks import crack_password_task
import time  # Import the time module

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/crack-password/", methods=["POST"])
def crack_password():
    data = request.json
    password = data.get("password")
    method = data.get("method")
    start_time = time.time()  # Now `time` is defined

    # Submit task to Celery
    task = crack_password_task.delay(password, method)

    # Wait for the task to complete
    cracked_password, success = task.get(timeout=300)  # 5 minutes timeout for the task

    duration = time.time() - start_time

    if not success:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Failed to crack the password or process timed out.",
                }
            ),
            500,
        )

    return jsonify(
        {"cracked_password": cracked_password, "duration": round(duration, 2)}
    )


if __name__ == "__main__":
    app.run(debug=False)
