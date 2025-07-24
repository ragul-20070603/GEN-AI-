
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_trending_skills(job_role):
    prompt = f"List 10 current in-demand technical skills for the role of a {job_role}. Give only comma-separated skills, no explanation."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return [skill.strip() for skill in response['choices'][0]['message']['content'].split(",")]
