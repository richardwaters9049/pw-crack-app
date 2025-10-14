<div align="center">

# 🔐 Password Cracker Web Application

### _A Retro Matrix-Themed Cybersecurity Demonstration Tool_

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2.5-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

**[Features](#-features) • [Quick Start](#-quick-start) • [Demo](#-what-it-does) • [Tech Stack](#-tech-stack) • [Contributing](#-future-enhancements)**

---

</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ What It Does](#-what-it-does)
- [🎨 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔒 Cybersecurity Insights](#-cybersecurity-insights)
- [🎓 Learning Outcomes](#-learning-outcomes)
- [🚧 Future Enhancements](#-future-enhancements)
- [🙏 Acknowledgements](#-acknowledgements)

## 🎯 Project Overview

> **A sleek, educational cybersecurity tool that brings the Matrix aesthetic to password security demonstrations.**

This web application showcases password-cracking techniques through an immersive retro Matrix-themed interface. Built with Flask and powered by Python, it features a streamlined architecture that processes password-cracking operations via subprocess calls—making it incredibly simple to deploy and run locally.

**Perfect for:** Security enthusiasts, students, educators, and developers interested in cybersecurity fundamentals.

---

## ✨ What It Does

<table>
<tr>
<td width="50%">

### 🎮 User Experience

1. 🔑 **Enter a password** to test its strength
2. ⚙️ **Select a cracking method** (Method 1 or Method 2)
3. ⏱️ **View results** with cracked password and time taken
4. 🌧️ **Enjoy the Matrix rain effect** during processing

</td>
<td width="50%">

### ⚡ Behind the Scenes

The backend processes password-cracking requests through a lightweight worker script that can be extended with:

- 📚 **Dictionary attacks**
- 🔨 **Brute-force methods**
- 🧮 **Character optimisation**
- 🚀 **Custom algorithms**

</td>
</tr>
</table>

---

## 🎨 Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🎭 **Matrix Theme** | Immersive retro interface with cascading green code |
| ⚡ **Fast Processing** | Optimised subprocess-based architecture |
| 📊 **Performance Metrics** | Real-time display of cracking duration |
| 🎨 **Responsive Design** | Tailwind CSS for modern, mobile-friendly UI |
| 🔤 **Custom Font** | Authentic Retro Computer typeface |
| 🌐 **Easy Deployment** | Simple setup with minimal dependencies |
| 🔧 **Extensible** | Modular design for adding new cracking methods |

</div>

---

## 🔒 Cybersecurity Insights

### 🎓 What You'll Learn

This application demonstrates fundamental cybersecurity concepts:

<table>
<tr>
<td width="50%">

#### 📚 Dictionary Attacks

- Highlights the danger of common passwords
- Shows why "password123" is a terrible choice
- Demonstrates the importance of unique passphrases
- **Lesson:** Never use easily guessable passwords!

</td>
<td width="50%">

#### 🔨 Brute-Force Attacks

- Reveals vulnerabilities in short passwords
- Demonstrates the power of character diversity
- Shows exponential complexity with length
- **Lesson:** Longer + diverse = stronger!

</td>
</tr>
</table>

### 🧮 Character Type Optimisation

The application includes intelligent character analysis to improve brute-force efficiency:

- 🔍 **Analyses password composition** (letters, digits, symbols)
- 🎯 **Narrows search space** based on detected character types
- ⚡ **Significantly reduces** cracking time for uniform passwords
- 💡 **Demonstrates** why diverse characters matter

> **Key Takeaway:** Understanding these techniques helps develop more secure password policies and improves overall system security.

---

## 🛠️ Tech Stack

<div align="center">

### Core Technologies

| Technology | Purpose | Version |
|------------|---------|--------|
| 🐍 **Python** | Backend language | 3.9+ |
| 🌶️ **Flask** | Web framework | 2.2.5 |
| 🦄 **Gunicorn** | Production server | 21.2.0 |
| 🎨 **Tailwind CSS** | Styling (CDN) | 2.2.19 |
| ✨ **JavaScript** | Matrix effects | ES6+ |

### Python Libraries

```python
subprocess  # Worker process management
json        # Data serialisation
time        # Performance metrics
```

</div>

---

## 🚀 Quick Start

### 📦 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### 💻 Installation

<details open>
<summary><b>🐧 macOS / Linux</b></summary>

```bash
# 1️⃣ Clone the repository
git clone https://github.com/richardwaters9049/pw-crack-app.git
cd pw-crack-app

# 2️⃣ Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the application
python3 app.py
```

</details>

<details>
<summary><b>🪟 Windows</b></summary>

```bash
# 1️⃣ Clone the repository
git clone https://github.com/richardwaters9049/pw-crack-app.git
cd pw-crack-app

# 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the application
python app.py
```

</details>

### 🌐 Access the Application

1. Open your browser
2. Navigate to: **http://127.0.0.1:5000**
3. Enter a password to test
4. Select a cracking method
5. Click **"Crack Password"** and watch the Matrix magic! ✨

### 🚀 Production Deployment

```bash
# Using Gunicorn (recommended)
gunicorn app:app --bind 0.0.0.0:8000

# Or specify workers for better performance
gunicorn app:app --workers 4 --bind 0.0.0.0:8000
```

---

## 📁 Project Structure

```text
pw-crack-app/
├── 🐍 app.py                    # Main Flask application
├── ⚙️ worker.py                 # Password cracking logic
├── 📦 requirements.txt          # Python dependencies
├── 🚀 Procfile                 # Deployment configuration
├── 📂 static/
│   ├── 🔤 fonts/               # Custom Retro Computer font
│   │   └── retro_computer_personal_use.ttf
│   ├── 🎨 style.css            # Custom styles with @font-face
│   ├── 📊 css/
│   │   └── output.css          # Compiled styles
│   └── ✨ matrix.js            # Matrix rain effect animation
└── 📄 templates/
    └── 🎭 index.html           # Main web interface
```

---

## 🎓 Learning Outcomes

By exploring this project, you'll gain hands-on experience with:

<table>
<tr>
<td width="50%">

### 🔐 Security Concepts
- Password vulnerability assessment
- Attack vector understanding
- Security best practices
- Risk mitigation strategies

</td>
<td width="50%">

### 💻 Technical Skills
- Flask web development
- Python subprocess management
- Frontend/backend integration
- Responsive UI design

</td>
</tr>
</table>

---

## 🚧 Future Enhancements

We're always looking to improve! Here's what's on the roadmap:

- [ ] 🧵 **Multithreading** - Further optimise brute-force performance
- [ ] 🔐 **User Authentication** - Save passwords and view cracking history
- [ ] 📊 **Password Strength Checker** - Real-time strength analysis
- [ ] 🔒 **Advanced Hashing** - Support for bcrypt, Argon2, and more
- [ ] 🎨 **Theme Customisation** - Multiple colour schemes
- [ ] 📱 **Mobile App** - Native iOS/Android versions
- [ ] 🌍 **Internationalisation** - Multi-language support
- [ ] 📈 **Analytics Dashboard** - Visualise cracking statistics
- [ ] 🤖 **AI-Powered Attacks** - Machine learning-based password prediction

---

## 🙏 Acknowledgements

This project wouldn't be possible without these amazing resources:

<div align="center">

| Resource | Contribution |
|----------|-------------|
| 🔗 **[SecLists](https://github.com/danielmiessler/SecLists)** | Comprehensive password lists for dictionary attacks |
| 🌶️ **[Flask](https://flask.palletsprojects.com/)** | Lightweight and powerful web framework |
| 🎨 **[Tailwind CSS](https://tailwindcss.com/)** | Beautiful utility-first CSS framework |
| 🦄 **[Gunicorn](https://gunicorn.org/)** | Production-ready WSGI server |
| 💚 **Open Source Community** | Inspiration and continuous learning |

</div>

---

<div align="center">

## 💡 Final Thoughts

> **"The best way to understand security is to think like an attacker."**

This project serves as a practical demonstration of password-cracking techniques and their implications in cybersecurity. By understanding these methods, we can better appreciate the importance of strong, unique passwords in protecting our digital assets.

**Remember:** Always use this tool responsibly and ethically. Never attempt to crack passwords you don't own or have explicit permission to test.

---

### 📝 Licence

This project is open source and available under the [MIT Licence](LICENSE).

### 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/richardwaters9049/pw-crack-app/issues).

### ⭐ Show Your Support

If you found this project helpful or interesting, please consider giving it a star! It helps others discover the project.

---

**Made with 💚 by [Richard Waters](https://github.com/richardwaters9049)**

**Happy Hacking! 🚀**

</div>
