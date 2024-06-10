from flask import Flask, render_template
import requests

app = Flask(__name__)

PROJECTS_API_URL = "https://portfolio-api-1zj4.onrender.com/api/v1/projects"
PROJECT_API_URL = "https://portfolio-api-1zj4.onrender.com/api/v1/projects/{}"

# Set timeout in seconds (adjust as needed)
REQUEST_TIMEOUT = 120  # 2 minutes

@app.route('/')
def homepage():
    try:
        projects = requests.get(PROJECTS_API_URL, timeout=REQUEST_TIMEOUT).json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching projects: {e}"
    return render_template('homepage.html', projects=projects)

@app.route('/project/<string:project_id>')
def project(project_id):
    try:
        project_details = requests.get(PROJECT_API_URL.format(project_id), timeout=REQUEST_TIMEOUT).json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching project details: {e}"
    return render_template('project.html', project=project_details)

if __name__ == '__main__':
    app.run(debug=False)
