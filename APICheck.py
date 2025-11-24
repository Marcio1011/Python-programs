"""
This script sends requests to a specified API endpoint, measures the response time,
captures the HTTP status code, and logs the results (URL, date, status, duration)
into a CSV file. It includes basic error handling for network failures, timeouts,
and write errors, making it useful for monitoring API health or performance over time.
"""

import sys
import re
from termcolor import colored, cprint
import requests
from jsonpath import jsonpath
import json
import csv
import time
import datetime

# Main entry point that initializes the process
def main():
    print(colored("This script sends requests to an API and measures response time.\n", 'yellow', 'on_grey'))
    print("\n")

    save_api_data('account.json')
    save_api_data('admin/modules/list.json')

# Function to send an API request and log timing/status results
def save_api_data(api_name):
    # Capture start time
    start = time.time()

    # Prepare a record list with URL and date
    result = ['<API_BASE_URL>/' + api_name, current_date()]
    print("Executing the API...")

    # Authentication header placeholder
    header = {"app-token": "<AUTH_TOKEN>"}

    # Build full URL
    url = '<API_BASE_URL>/' + api_name

    # Example query parameters
    param = {"name": "<GENERIC_ID>"}

    # Print request details
    print(url + str(param) + str(header))

    try:
        # Perform HTTP GET with timeout
        profile = requests.get(url, params=param, headers=header, timeout=10)

        # Capture end time
        end = time.time()

        # Calculate duration
        total = end - start

        # Store HTTP status code
        result.append(profile.status_code)
        print(profile.status_code)

        # Store runtime
        result.append(total)
        print("The API runtime is", total, "Sec")

        # Check for non-success response
        if profile.status_code >= 400:
            print(colored("Warning: API returned an error status code.", "red"))

    except requests.exceptions.Timeout:
        print(colored("Error: The API request timed out.", "red"))
        return

    except requests.exceptions.ConnectionError:
        print(colored("Error: Failed to connect to the API endpoint.", "red"))
        return

    except requests.exceptions.RequestException as e:
        print(colored(f"Unexpected request error: {e}", "red"))
        return

    # Write results to CSV
    try:
        print(colored('Writing the data to the CSV file...', 'blue', 'on_grey'))
        with open("apis.csv", "a+", newline="") as file:
            f = csv.writer(file)
            f.writerow(result)
    except IOError:
        print(colored("Error: Could not write to CSV file.", "red"))

# Function to return today's date
def current_date():
    today = datetime.date.today()
    print(today)
    return today

# Run main only when executed directly
if __name__ == "__main__":
    main()
