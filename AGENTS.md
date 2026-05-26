# Agents

This document provides guidance for AI agents and contributors working on this project.

## Project Overview

A Flask-based web application that demonstrates password-cracking techniques (dictionary attacks and brute-force methods) through an interactive, Matrix-themed interface. Built for educational purposes to illustrate cybersecurity fundamentals.

## Tech Stack

- **Backend:** Python 3.9+, Flask 2.2.5
- **Frontend:** HTML (Jinja2 templates), Tailwind CSS (CDN), vanilla JavaScript
- **Production server:** Gunicorn
- **Styling:** Custom CSS with a retro computer font, Matrix rain animation

## Project Structure

```
pw-crack-app/
├── app.py                  # Flask application (routes and request handling)
├── worker.py               # Password-cracking logic (called via subprocess)
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn deployment config
├── static/
│   ├── fonts/              # Custom Retro Computer typeface
│   ├── style.css           # Global styles and font-face declarations
│   ├── css/output.css      # Compiled styles
│   └── matrix.js           # Matrix rain background animation
└── templates/
    └── index.html          # Main (and only) page template
```

## Local Development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m flask --app app run --debug
```

The application will be available at `http://localhost:5000`.

## Conventions

- **Language:** UK English throughout code comments, documentation, and UI text.
- **Formatting:** HTML uses 2-space indentation. Python follows PEP 8.
- **Frontend:** Tailwind CSS utility classes via CDN; no build step required. JavaScript is vanilla ES6+ inlined in the template.
- **Method descriptions:** Defined in a single JavaScript object (`methods`) in `templates/index.html`. To add or modify cracking method descriptions, update this object only — the HTML elements are populated dynamically.
- **Backend architecture:** The Flask app delegates password-cracking work to `worker.py` via `subprocess.run()`. New cracking methods should be implemented in `worker.py`.

## Deployment

Production deployment uses Gunicorn as specified in the `Procfile`:

```bash
gunicorn app:app --bind 0.0.0.0:8000
```

## Key Notes

- There is no test suite currently configured.
- There is no CI/CD pipeline.
- There are no pre-commit hooks.
- The project has a single HTML page (`templates/index.html`) serving as the entire frontend.
