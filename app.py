
from flask import Flask, request, jsonify
from flask_cors import CORS
from text_extractor import extract_text_from_file
from skill_matcher import compare_skills
from trending_skills import get_trending_skills
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files or "job_role" not in request.form:
        return jsonify({"error": "Missing file or job role"}), 400

    resume_file = request.files["resume"]
    job_role = request.form["job_role"]

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        resume_file.save(tmp.name)
        resume_text = extract_text_from_file(tmp.name)
        os.unlink(tmp.name)

    job_skills = get_trending_skills(job_role)
    match_rate, matched, unmatched = compare_skills(resume_text, job_skills)

    return jsonify({
        "match_rate": match_rate,
        "matched_skills": matched,
        "missing_skills": unmatched,
        "trending_skills": job_skills
    })

if __name__ == "__main__":
    app.run(debug=True)
