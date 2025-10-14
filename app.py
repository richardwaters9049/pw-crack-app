from flask import Flask, request, jsonify, render_template
import subprocess
import json
import time
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/crack-password/", methods=["POST"])
def crack_password():
    data = request.json
    password = data.get("password")
    method = data.get("method")
    start_time = time.time()

    try:
        # Call worker.py directly instead of using Celery
        result = subprocess.run(
            ["python3", "worker.py", password, method],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minutes timeout
        )
        
        if result.returncode == 0:
            result_json = json.loads(result.stdout)
            cracked_password = result_json.get("password")
            duration = time.time() - start_time
            
            return jsonify(
                {"cracked_password": cracked_password, "duration": round(duration, 2)}
            )
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Failed to crack the password.",
                    }
                ),
                500,
            )
    except subprocess.TimeoutExpired:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Process timed out.",
                }
            ),
            500,
        )
    except json.JSONDecodeError:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Error decoding result.",
                }
            ),
            500,
        )


if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=False)  # Bind to 0.0.0.0
