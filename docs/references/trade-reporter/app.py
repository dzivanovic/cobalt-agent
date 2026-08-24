import uuid
from pathlib import Path

from flask import Flask, render_template, request, jsonify, send_file

from utils.drc_builder import build_drc_pdf
from utils.playbook_builder import build_playbook

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # screenshots can be heavy

TMP_DIR = Path(__file__).parent / "tmp"
TMP_DIR.mkdir(exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/build-drc", methods=["POST"])
def build_drc():
    data = request.get_json(force=True) or {}
    try:
        pdf_bytes = build_drc_pdf(data)
    except Exception as e:
        return jsonify({"error": f"PDF error: {e}"}), 500
    session_id = str(uuid.uuid4())
    path = TMP_DIR / f"{session_id}.pdf"
    path.write_bytes(pdf_bytes)
    return jsonify({"session_id": session_id, "ext": "pdf"})


@app.route("/build-playbook", methods=["POST"])
def build_pb():
    data = request.get_json(force=True) or {}
    try:
        pptx_bytes = build_playbook(data)
    except Exception as e:
        return jsonify({"error": f"PPTX error: {e}"}), 500
    session_id = str(uuid.uuid4())
    path = TMP_DIR / f"{session_id}.pptx"
    path.write_bytes(pptx_bytes)
    return jsonify({"session_id": session_id, "ext": "pptx"})


@app.route("/download/<session_id>/<ext>")
def download(session_id: str, ext: str):
    if ext not in ("pdf", "pptx"):
        return "Invalid type", 400
    path = TMP_DIR / f"{session_id}.{ext}"
    if not path.exists():
        return "File not found or expired.", 404
    names = {"pdf": "bigscalp_edge_daily_report_card.pdf", "pptx": "bigscalp_edge_playbook.pptx"}
    mimes = {
        "pdf": "application/pdf",
        "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    }
    return send_file(path, as_attachment=True,
                     download_name=names[ext], mimetype=mimes[ext])


@app.route("/view/<session_id>.pdf")
def view_pdf(session_id: str):
    path = TMP_DIR / f"{session_id}.pdf"
    if not path.exists():
        return "File not found or expired.", 404
    return send_file(path, as_attachment=False, mimetype="application/pdf")


if __name__ == "__main__":
    import sys
    no_reload = "--no-reload" in sys.argv
    app.run(port=5002, debug=not no_reload, use_reloader=not no_reload)
