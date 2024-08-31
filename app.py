import itertools
import string
import hashlib
import time
from multiprocessing import Pool, cpu_count
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Constants
PASSWORD_LIST_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt"


def check_password_type(password):
    """
    Analyze the password to determine its character composition.
    Returns the appropriate character set based on the composition.
    """
    if password.isdigit():
        return string.digits  # Only digits
    elif password.isalpha():
        return string.ascii_letters  # Only letters
    elif password.isalnum():
        return string.ascii_letters + string.digits  # Letters and digits
    else:
        return string.printable  # All possible characters


def hash_password(password, method="md5"):
    """
    Hash a password using the specified method.
    """
    if method == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash method")


def dictionary_attack(hashed_password, method):
    """
    Perform a dictionary attack using an online password list.
    """
    response = requests.get(PASSWORD_LIST_URL)
    common_passwords = response.text.splitlines()

    for password in common_passwords:
        if hash_password(password, method) == hashed_password:
            return password
    return None


def brute_force_attack(hashed_password, char_set, max_length, method):
    """
    Perform a brute-force attack using the specified character set.
    """
    for length in range(1, max_length + 1):
        for attempt in itertools.product(char_set, repeat=length):
            attempt_password = "".join(attempt)
            if hash_password(attempt_password, method) == hashed_password:
                return attempt_password
    return None


def crack_password_parallel(password, method="md5", url=None):
    """
    Attempt to crack the password using both dictionary and brute-force attacks.
    """
    hashed_password = hash_password(password, method)
    char_set = check_password_type(password)
    start_time = time.time()

    # Attempt dictionary attack first
    cracked_password = dictionary_attack(hashed_password, method)
    if cracked_password:
        duration = time.time() - start_time
        return cracked_password, duration

    # Fall back to brute-force attack
    max_length = len(password)
    pool = Pool(processes=cpu_count())

    result = pool.apply_async(
        brute_force_attack, (hashed_password, char_set, max_length, method)
    )
    cracked_password = result.get()

    duration = time.time() - start_time
    return cracked_password, duration


@app.route("/", methods=["GET", "POST"])
def index():
    cracked_password = None
    duration = None

    if request.method == "POST":
        password = request.form["password"]
        method = request.form["method"]
        cracked_password, duration = crack_password_parallel(password, method)

    return render_template(
        "index.html", cracked_password=cracked_password, duration=round(duration, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
