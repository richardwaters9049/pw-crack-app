from flask import Flask, request, jsonify, render_template
from tasks import crack_password_task
import time  # Import the time module
import os  # Import os module for environment variables

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
    # Bind to 0.0.0.0 and use the PORT environment variable
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=False)  # Bind to 0.0.0.0
