import json
from pathlib import Path
from flask import Blueprint, render_template, jsonify, abort

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data" / "content.json").read_text(encoding="utf-8"))

PAGE_KEYS = ["main", "subject", "rationale", "features", "environment", "team"]

pages_bp = Blueprint("pages", __name__)
api_bp = Blueprint("api", __name__)

# HTML Pages
@pages_bp.route("/")
@pages_bp.route("/main")
def main_page():
    return render_template("main.html", data=DATA.get("main", {}), pages=PAGE_KEYS)

@pages_bp.route("/subject")
def subject_page():
    return render_template("subject.html", data=DATA.get("subject", {}), pages=PAGE_KEYS)

@pages_bp.route("/rationale")
def rationale_page():
    return render_template("rationale.html", data=DATA.get("rationale", {}), pages=PAGE_KEYS)

@pages_bp.route("/features")
def features_page():
    return render_template("features.html", data=DATA.get("features", {}), pages=PAGE_KEYS)

@pages_bp.route("/environment")
def environment_page():
    return render_template("environment.html", data=DATA.get("environment", {}), pages=PAGE_KEYS)

@pages_bp.route("/team")
def team_page():
    return render_template("team.html", data=DATA.get("team", {}), pages=PAGE_KEYS)

# APIs
@api_bp.route("/<page>")
def page_api(page):
    if page not in PAGE_KEYS:
        abort(404)
    return jsonify(DATA.get(page, {}))
