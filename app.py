from flask import Flask, request, render_template
import hashlib
import itertools
import string
import requests
import multiprocessing
import time


app = Flask(__name__)

# URL to the large password list
PASSWORD_LIST_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt"


def fetch_passwords_from_url(url):
    """
    Fetches a list of passwords from a provided URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        # Return passwords as a list of strings
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Error fetching password list: {e}")
        return []


def dictionary_attack(password_hash, method="md5", url=PASSWORD_LIST_URL):
    """
    Attempts to crack the password using a dictionary attack with passwords from an online URL.
    """
    passwords = fetch_passwords_from_url(url)
    for word in passwords:
        word = word.strip()
        # Compare the hash of the password with the target hash
        if hashlib.md5(word.encode("utf-8")).hexdigest() == password_hash:
            return word
    return None


def worker(chars, password_hash, method, length, start, end, return_dict, index):
    """
    Worker function for brute-force password cracking using multiple processes.
    """
    for guess in itertools.product(chars, repeat=length):
        guess_str = "".join(guess)
        if hashlib.md5(guess_str.encode("utf-8")).hexdigest() == password_hash:
            return_dict[index] = guess_str
            return


def crack_password_parallel(password, method="md5", url=PASSWORD_LIST_URL):
    """
    Attempts to crack the password using parallel brute-force processing.
    """
    chars = string.ascii_lowercase + string.digits + string.punctuation
    length = len(password)
    password_hash = hashlib.md5(password.encode("utf-8")).hexdigest()

    # Record the start time
    start_time = time.time()

    # First try the dictionary attack
    result = dictionary_attack(password_hash, method, url)
    if result:
        # Record end time and calculate duration
        end_time = time.time()
        duration = end_time - start_time
        return result, duration

    # If not found, perform parallel brute-force attack
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    num_workers = multiprocessing.cpu_count()

    # Create and start worker processes
    for i in range(num_workers):
        p = multiprocessing.Process(
            target=worker,
            args=(chars, password_hash, method, length, i, num_workers, return_dict, i),
        )
        jobs.append(p)
        p.start()

    # Wait for all worker processes to finish
    for p in jobs:
        p.join()

    # Record end time and calculate duration
    end_time = time.time()
    duration = end_time - start_time

    # Check results from the processes
    for i in range(num_workers):
        if i in return_dict:
            return return_dict[i], duration

    return None, duration


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Route handler for the main page. Processes password submissions and displays results.
    """
    cracked_password = None
    duration = None
    if request.method == "POST":
        password = request.form["password"]
        method = request.form.get("method", "md5")
        result, duration = crack_password_parallel(password, method, PASSWORD_LIST_URL)
        cracked_password = result
        # Format duration to two decimal places
        if duration is not None:
            duration = f"{duration:.2f}"
        return render_template(
            "index.html", cracked_password=cracked_password, duration=duration
        )
    return render_template("index.html")


if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
