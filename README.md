# Password Cracker Web Application

A cybersecurity demonstration tool that showcases common password-cracking techniques through an interactive web interface with a retro Matrix theme.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2.5-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Licence](https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge)](LICENSE)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Aim](#project-aim)
- [Expected Outcome](#expected-outcome)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Cybersecurity Context](#cybersecurity-context)
- [Future Enhancements](#future-enhancements)
- [Licence](#licence)

---

## Project Overview

This web application provides a practical, hands-on demonstration of how password-cracking techniques function. It is designed as an educational tool for security enthusiasts, students, and developers who want to understand the mechanics behind common attack vectors — and, by extension, why strong passwords matter.

The application presents a clean, immersive interface inspired by the Matrix film aesthetic, with cascading green characters animating in the background whilst the user interacts with the cracking tool.

---

## Project Aim

The primary aim of this project is to **demystify password-cracking methods** in a safe, controlled environment. Specifically, it seeks to:

1. **Educate users** on how dictionary attacks and brute-force attacks operate in practice.
2. **Demonstrate the relationship** between password complexity and the time required to crack it.
3. **Encourage better security habits** by showing how quickly weak passwords can be compromised.
4. **Provide a foundation** for further exploration of cybersecurity concepts, including character-set optimisation and algorithmic approaches to password analysis.

---

## Expected Outcome

After using the application, users should:

- Understand the difference between dictionary-based and brute-force cracking methods.
- Appreciate why short, simple, or commonly-used passwords are inherently vulnerable.
- Recognise the importance of password length, character diversity, and uniqueness.
- Be motivated to adopt stronger password practices in their own digital lives.

---

## How It Works

The application follows a straightforward client-server architecture:

1. **User input** — The user enters a password and selects a cracking method (dictionary attack or brute-force) via the web interface.
2. **Form submission** — The frontend sends a POST request to the Flask backend with the password and chosen method.
3. **Worker process** — The Flask application delegates the cracking operation to `worker.py` via a subprocess call. This keeps the main application responsive and modular.
4. **Result** — The worker returns the cracked password (or an error), along with the time taken. This is displayed to the user in real time.
5. **Reset** — After displaying results, a countdown timer resets the interface for the next attempt.

### Cracking Methods

| Method | Approach | Description |
|--------|----------|-------------|
| **Method 1 — Dictionary Attack** | Wordlist comparison | Tests the input against a list of commonly used passwords. Fast for weak passwords that appear in known wordlists. |
| **Method 2 — Brute-Force Attack** | Exhaustive search | Systematically tries all possible character combinations until a match is found. Slower, but guaranteed to find the password given enough time. |

---

## Features

- **Matrix-themed interface** — Cascading green character animation providing an immersive retro aesthetic.
- **Responsive design** — Mobile-friendly layout built with Tailwind CSS.
- **Real-time performance metrics** — Displays cracking duration so users can compare method efficiency.
- **Dynamic method descriptions** — Contextual information updates as the user selects different cracking methods.
- **Custom typography** — Retro Computer font for an authentic terminal feel.
- **Modular architecture** — Cracking logic is separated into a worker script, making it straightforward to add new methods.
- **Lightweight deployment** — Minimal dependencies; runs locally with a single command.

---

## Tech Stack

| Technology | Role | Version |
|------------|------|---------|
| Python | Backend language | 3.9+ |
| Flask | Web framework | 2.2.5 |
| Gunicorn | Production WSGI server | 21.2.0 |
| Tailwind CSS | Utility-first styling (CDN) | 2.2.19 |
| JavaScript (ES6+) | Matrix animation and UI logic | — |
| Jinja2 | HTML templating | 3.1.3 |

### Python Standard Library Usage

- `subprocess` — Manages the worker process for password cracking.
- `json` — Handles data serialisation between the Flask app and the worker.
- `time` — Measures cracking duration for performance reporting.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/richardwaters9049/pw-crack-app.git
cd pw-crack-app

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
python3 -m flask --app app run --debug
```

The application will be available at **http://localhost:5000**.

The `--debug` flag enables auto-reload, so any file changes will be reflected immediately without restarting the server.

---

## Project Structure

```
pw-crack-app/
├── app.py                  # Flask application — routes and request handling
├── worker.py               # Password-cracking logic (invoked via subprocess)
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn deployment configuration
├── AGENTS.md               # Agent/contributor guidance
├── static/
│   ├── fonts/              # Custom Retro Computer typeface
│   ├── style.css           # Global styles and @font-face declarations
│   ├── css/output.css      # Compiled styles
│   └── matrix.js           # Matrix rain background animation
└── templates/
    └── index.html          # Main page template (single-page application)
```

---

## Deployment

The application is production-ready with Gunicorn. A `Procfile` is included for platforms such as Heroku and Render.

```bash
# Standard deployment
gunicorn app:app --bind 0.0.0.0:8000

# With multiple workers for improved throughput
gunicorn app:app --workers 4 --bind 0.0.0.0:8000
```

---

## Cybersecurity Context

### Dictionary Attacks

A dictionary attack works by comparing the target password against a precompiled list of known, commonly-used passwords (e.g., "password123", "qwerty", "letmein"). If the password appears in the list, it is cracked almost instantly. This method highlights why users should avoid predictable passwords and why organisations maintain blocklists of compromised credentials.

### Brute-Force Attacks

A brute-force attack exhaustively generates and tests every possible combination of characters until the correct password is found. While guaranteed to succeed eventually, the time required grows exponentially with password length and character-set diversity. A four-character numeric password has only 10,000 possible combinations; an eight-character alphanumeric password with symbols has over 6 quadrillion.

### Character-Set Optimisation

The application analyses the composition of the target password to narrow the search space during brute-force operations. If the password contains only lowercase letters, for example, the algorithm skips digits and symbols entirely — significantly reducing cracking time. This demonstrates precisely why using a diverse character set (uppercase, lowercase, digits, and symbols) is critical for password security.

### Key Takeaway

Understanding how these attacks work is essential for developing robust security policies. The faster a password can be cracked, the weaker it is. Users should aim for passwords that are long, unique, and composed of diverse character types.

---

## Future Enhancements

- Multithreading for improved brute-force performance
- Password strength analyser with real-time feedback
- Support for additional hashing algorithms (bcrypt, Argon2)
- User authentication and cracking history
- Analytics dashboard for visualising cracking statistics
- Expanded wordlists and rule-based mutations for dictionary attacks

---

## Licence

This project is open source and available under the [MIT Licence](LICENSE).

---

## Contributing

Contributions, issues, and feature requests are welcome. Please check the [issues page](https://github.com/richardwaters9049/pw-crack-app/issues) for current discussions.

---

**Important:** This tool is intended solely for educational purposes. Never attempt to crack passwords that you do not own or have explicit permission to test.
