import os
import subprocess
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/run-script", methods=["GET"])
def runScript():
    try:
        command = ["python3", "main.py"]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}", 200
    except Exception as e:
        return f"Failed to run the script {str(e)}", 500


         