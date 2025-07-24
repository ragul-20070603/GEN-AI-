
def compare_skills(resume_text, job_skills):
    matched = [skill for skill in job_skills if skill.lower() in resume_text.lower()]
    unmatched = [skill for skill in job_skills if skill not in matched]
    match_rate = len(matched) / len(job_skills) * 100
    return match_rate, matched, unmatched
