#!/usr/bin/env python

# This script reads a JSON-lines text file and converts each JSON entry into a row in a CSV file.

import json
import csv

# Open the source text file containing JSON objects (one per line)
sdrs_file = open('events.txt')

# Open or create the CSV file for writing data
sdrs = open("events.csv", 'wb')

# Create a CSV writer object using Excel-compatible formatting
wr = csv.writer(sdrs, dialect='excel')

# Write the header row for the CSV file
wr.writerow(['timestamp', 'user', 'activity'])

# Loop through each line in the JSON-lines file
for line in sdrs_file:
    # Convert the JSON-formatted string into a Python dictionary
    sdr_json = json.loads(line)

    # Write selected fields into a corresponding CSV row
    wr.writerow([sdr_json['timestamp'], sdr_json['user'], sdr_json['activity']])



	


	

