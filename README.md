# Password Cracker Web Application

## Project Overview

This project is a web application designed to demonstrate password-cracking techniques, specifically through a combination of dictionary attacks and brute-force methods. The application is built using Flask, a lightweight Python web framework, and utilizes Python's standard libraries for hashing and multiprocessing. It also integrates Tailwind CSS for styling to ensure a modern and responsive user interface.

## What the Application Does

The application allows users to input a password and then attempts to crack it by:

1. **Dictionary Attack**: Uses a large list of common passwords fetched from an online source.
2. **Brute-Force Attack**: Iterates through all possible combinations of characters to find a match, leveraging parallel processing to speed up the process.

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

- **Flask**: Web framework for Python.
- **Requests**: Library for making HTTP requests to fetch the password list.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **Python Standard Libraries**: `hashlib`, `itertools`, `string`, and `multiprocessing` for password cracking functionalities.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pw-crack-app.git
   cd pw-crack-app
   ```
2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip3 install flask requests
   ```
4. **Run the Application**:
   ```bash
   python3 app.py
   ```
5. **Access the Web Interface**:
   Open a web browser and navigate to http://127.0.0.1:5000

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

Feel free to adjust any details according to your specific setup or preferences.
