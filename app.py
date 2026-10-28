from pathlib import Path
from flask import Flask, send_from_directory, jsonify

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="/static")


@app.route("/")
def home():
    """Serve the F1 Racing Intelligence website."""
    index_file = BASE_DIR / "index.html"
    if not index_file.exists():
        return (
            "index.html was not found. Place index.html in the same folder as app.py.",
            404,
        )
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/health")
def health():
    """Simple endpoint to check whether the Flask app is running."""
    return jsonify(status="ok", app="F1 Racing Intelligence")


if __name__ == "__main__":
    # Local development server. For production, use a production WSGI server.
    app.run(host="127.0.0.1", port=5000, debug=True)
