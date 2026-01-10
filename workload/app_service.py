from flask import Flask, jsonify
from batch_logic import run_simulation
import threading

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/run-simulation", methods=["POST"])
def trigger_simulation():
    # Run simulation in background so API doesn't block
    thread = threading.Thread(target=run_simulation)
    thread.start()

    return jsonify({"message": "Simulation started"}), 202

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

