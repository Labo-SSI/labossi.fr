from flask import Flask, render_template, send_from_directory
from flask_talisman import Talisman
import os

app = Flask(__name__)
# csp = {
#     'default-src': "'self'",
#     'script-src': [
#         "'self'",
#         'https://cdn.tailwindcss.com',
#         "'unsafe-inline'"  # This allows inline scripts
#     ],
#     'style-src': [
#         "'self'",
#         'https://cdn.tailwindcss.com',
#         "'unsafe-inline'"  # This allows inline styles
#     ]
# }
# Talisman(app, content_security_policy=csp)

# Upcoming workshop details
workshop = {
    "title": "Advanced Network Security",
    "description": "Learn about the latest techniques in network security and how to implement them.",
    "instructor": "Jane Doe, CISSP",
    "date": "July 15, 2023",
    "time": "2:00 PM - 5:00 PM",
    "signup_link": "https://forms.gle/exampleGoogleFormLink"
}

# Upcoming CTFs
ctfs = [
    {"name": "DEF CON CTF", "date": "August 10-13, 2023"},
    {"name": "CSAW CTF", "date": "September 15-17, 2023"},
    {"name": "picoCTF", "date": "October 1-15, 2023"}
]

# Upcoming guests
guests = [
    {"name": "John Smith", "title": "Senior Security Researcher at TechCorp"},
    {"name": "Alice Johnson", "title": "Ethical Hacker and Bug Bounty Hunter"},
    {"name": "Bob Williams", "title": "Cybersecurity Professor at Cyber University"}
]

# Projects
projects = [
    {
        "name": "CTF Team",
        "description": "Participate in Capture The Flag competitions to enhance our skills."
    },
    {
        "name": "Open Source Forensic Tool",
        "description": "Developing a forensic analysis tool for the cybersecurity community."
    },
    {
        "name": "CTF Creation",
        "description": "Design and host our own Capture The Flag challenges."
    },
    {
        "name": "Bug Bounty Program",
        "description": "Collaborate on finding and reporting security vulnerabilities in real-world applications."
    },
    {
        "name": "CVE Research",
        "description": "Conduct code reviews on open-source projects to identify potential vulnerabilities and submit CVEs."
    }
]

@app.route('/')
def index():
    return render_template('index.html', workshop=workshop, ctfs=ctfs, guests=guests)

@app.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)

@app.route('/flag.txt')
def flag():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'flag.txt')

if __name__ == '__main__':
    app.run(debug=False)