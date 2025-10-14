# Password Cracker Web Application

<!-- ![Password Crack](/public/images/img.png "Matrix Style") -->

## Table of Contents

- [Password Cracker Web Application](#password-cracker-web-application)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [What the Application Does](#what-the-application-does)
  - [Character Type Optimization](#character-type-optimization)
    - [How It Relates to Cybersecurity](#how-it-relates-to-cybersecurity)
  - [Implementation Details](#implementation-details)
    - [GitHub Password List Integration](#github-password-list-integration)
    - [Attacks Used](#attacks-used)
    - [Features](#features)
    - [Dependencies](#dependencies)
    - [Setup Instructions](#setup-instructions)
    - [Acknowledgments](#acknowledgments)
    - [Summary](#summary)
    - [Conclusion](#conclusion)
    - [Future Enhancements](#future-enhancements)

## Project Overview

This project is a web application designed to demonstrate password-cracking techniques. The application is built using Flask, a lightweight Python web framework, with a retro Matrix-style interface. It features a simple architecture that runs password cracking operations directly through subprocess calls, making it easy to deploy and run locally.

## What the Application Does

The application provides a retro Matrix-themed interface where users can:

1. Enter a password to test
2. Select a cracking method (Method 1 or Method 2)
3. View the cracked password and time taken
4. Experience a cool Matrix rain effect during processing

The backend processes password cracking requests through a simple worker script that can be extended with various cracking techniques such as dictionary attacks or brute-force methods.

## Character Type Optimization

A character type analysis has been implemented to improve the efficiency of the brute-force attack. This enhancement involves analyzing the password to determine if it contains only letters, only digits, or a combination of both. Based on this analysis, the application narrows down the brute-force search space to a specific set of characters, significantly reducing the time required to crack the password. This optimization is particularly effective for passwords with uniform character types, helping to demonstrate the importance of diverse character usage in password creation.

### How It Relates to Cybersecurity

This application showcases fundamental techniques in cybersecurity related to password cracking:

- **Dictionary Attacks**: Highlight the importance of not using common or easily guessable passwords.
- **Brute-Force Attacks**: Demonstrate the potential vulnerabilities in passwords that are too short or lack complexity.

Understanding these techniques helps in developing more secure password policies and improving overall system security.

## Implementation Details

### GitHub Password List Integration

Instead of maintaining a local file with common passwords, we dynamically fetch a large password list from GitHub. The list used is located at:

- **URL**: [xato-net-10-million-passwords-1000000.txt](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt)

This approach ensures that the application uses a comprehensive and up-to-date set of passwords without requiring large local storage.

### Attacks Used

1. **Dictionary Attack**:

   - **Implementation**: We fetch the password list from the provided GitHub URL and compare each password against the hashed input.
   - **Reason**: Dictionary attacks are effective against passwords that are common or easily guessable, highlighting the importance of using unique passwords.

2. **Brute-Force Attack**:
   - **Implementation**: Utilizes Python’s `itertools.product` to generate all possible combinations of characters up to the length of the input password. The process is parallelized using Python’s `multiprocessing` module to improve performance.
   - **Reason**: Brute-force attacks are used to demonstrate the potential weakness of shorter passwords or those with limited character sets.

### Features

- **Web Interface**: Simple and user-friendly web interface using Flask.
- **Performance Metrics**: Displays the time taken to crack the password.
- **Responsive Design**: Styled with Tailwind CSS for a modern look.

### Dependencies

- **Flask**: Web framework for Python
- **Gunicorn**: Production WSGI server (for deployment)
- **Tailwind CSS**: Utility-first CSS framework (loaded via CDN)
- **Python Standard Libraries**: `subprocess`, `json`, `time` for password cracking operations

### Setup Instructions

#### Quick Start (3 Steps)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/richardwaters9049/pw-crack-app.git
   cd pw-crack-app
   ```

2. **Create Virtual Environment and Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python3 app.py
   ```

4. **Access the Web Interface**:
   - Open your browser and navigate to: **http://127.0.0.1:5000**
   - Enter a password and select a cracking method
   - Click "Crack Password" to see the results!

#### Alternative: Run with Virtual Environment Python

```bash
# After step 2 above, you can also run:
venv/bin/python app.py
```

#### For Production Deployment

```bash
gunicorn app:app
```

### Project Structure

```text
pw-crack-app/
├── app.py                 # Main Flask application
├── worker.py              # Password cracking logic
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── static/
│   ├── fonts/            # Custom Retro Computer font
│   ├── style.css         # Custom styles
│   └── matrix.js         # Matrix rain effect
└── templates/
    └── index.html        # Main web interface
```

### Acknowledgments

- **SecLists**: For providing the extensive password list used in the dictionary attack.
- **Flask**: For the web framework.
- **Tailwind CSS**: For the styling framework.

### Summary

- **Project Overview**: Brief introduction to the project.
- **Application Description**: Details on what the application does and its relevance to cybersecurity.
- **Implementation**: How the GitHub link is used and the types of attacks implemented.
- **Setup Instructions**: Steps to get the project running on a local machine.
- **Contributing and License**: Information on contributing and licensing.

### Conclusion

This project serves as a practical demonstration of password cracking techniques and their implications in cybersecurity. By understanding these techniques, we can better appreciate the importance of strong and unique passwords in protecting our digital assets.

### Future Enhancements

- **Multithreading**: Implement multithreading to further speed up the brute-force attack.
- **User Authentication**: Implement user authentication to allow users to save their passwords and view their cracking history.
- **Password Strength Checker**: Integrate a password strength checker to encourage users to use more secure passwords.
- **Password Hashing**: Use a more secure hashing algorithm for password storage.
- **Error Handling**: Improve error handling and user feedback for a better user experience.
