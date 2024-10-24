from flask import Flask, render_template, send_from_directory, jsonify
import requests
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# Upcoming workshop details
workshop = {
    "title": "Les bases de l'analyse forensique sur la mémoire",
    "description": "Prérequis: Une machine linux, Python 3.8 ou supérieur",
    "prof": "Léo Rouger",
    "date": "23 Octobre 2024",
    "max_pers": "10",
    "lien": "https://docs.google.com/forms/d/e/1FAIpQLSeA_tahWQggtCUo5YLiLijGbJvLxM82_mOQ2eCjQsr8XCkMXA/viewform?usp=sf_link"
}

cached_ctf_data = None
last_fetched_time = None
CACHE_DURATION = 24 * 60 * 60

def fetch_ctf_data():
    global cached_ctf_data, last_fetched_time

    if cached_ctf_data and last_fetched_time:
        time_since_last_fetch = time.time() - last_fetched_time
        if time_since_last_fetch < CACHE_DURATION:
            return cached_ctf_data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux i640) Gecko/20100101 Firefox/47.3'
    }
    try:
        response = requests.get(
            f'https://ctftime.org/api/v1/events/?limit=4&start={int(time.time())}&finish={int((datetime.now() + timedelta(days=10)).timestamp())}', 
            headers=headers
        )
        response.raise_for_status()
        cached_ctf_data = response.json()
        last_fetched_time = time.time()
        return cached_ctf_data

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

def format_date(iso_date):
    parsed_date = datetime.fromisoformat(iso_date.rstrip('Z'))
    return parsed_date.strftime('%B %d, %Y')

@app.route('/')
def index():
    ctf_data = fetch_ctf_data()

    if ctf_data:
        ctfs = [
            {"name": event['title'], "date": format_date(event['start']), "url": event['url']} for event in ctf_data
        ]
    else:
        ctfs = [
            {"name": "Cannot update", "date": "", "url": "#"}
           
        ]

    return render_template('index.html', workshop=workshop, ctfs=ctfs, guests=guests)

guests = [
    # {"name": "Coming soon", "title": ""},
    # {"name": "Coming soon", "title": ""},
    # {"name": "Coming soon", "title": ""}
]


projects = [
    {
        "name": "Équipe CTF",
        "description": "Participer à des compétitions Capture The Flag pour améliorer nos compétences."
    },
    {
        "name": "Outil Forensique Open Source",
        "description": "Développer un outil d'analyse forensique pour la communauté de la cybersécurité."
    },
    {
        "name": "Création de CTF",
        "description": "Concevoir et organiser nos propres challs Capture The Flag."
    },
    {
        "name": "Programme de Bug Bounty",
        "description": "Collaborer pour identifier et signaler des vulnérabilités de sécurité dans des applications réelles."
    },
    {
        "name": "Recherche CVE",
        "description": "Effectuer des revues de code sur des projets open source pour identifier des vulnérabilités potentielles et soumettre des CVE."
    }
]

@app.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)

@app.route('/flag.txt')
def flag():
    return send_from_directory('static', 'flag.txt')

if __name__ == '__main__':
    app.run(debug=False)
