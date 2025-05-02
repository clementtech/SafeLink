# Importing the required libraries
# vt is the VirusTotal API client library
# os is used to interact with the operating system
# sys is used to exit the program if an error occurs
# dotenv is used to load environment variables from a .env file
# tabulate is used to create a table for displaying results

import os
import sys


# Check if the required modules are installed and if the API key is set
# If not, exit the program with an error message
try:

    import vt
    from dotenv import load_dotenv
    from tabulate import tabulate
    from google import genai

    # Load environment variables from .env file
    # This file should contain the API key for VirusTotal
    load_dotenv()
    # Get the API key from the environment variable
    # The API key should be stored in a .env file in the same directory as this script
    # The .env file should contain a line like "API_KEY=your_api_key_here"
    # If the API key is not set, a ValueError will be raised
    API_KEY_VT = os.getenv("API_KEY_VT")
    API_KEY_Google = os.getenv("API_KEY_Google")
    client_vt = vt.Client(API_KEY_VT)
    client_google = genai.Client(api_key = API_KEY_Google)

 

# If the API key is not set, exit the program with an error message
except ValueError:
    sys.exit("Please setup your API key in the .env file.")

# If the required modules are not installed, exit the program with an error message
except ModuleNotFoundError:
    sys.exit("Please install the required modules using 'pip install -r requirements.txt'.")

# If the API key is set, proceed with the URL scanning
# The user is prompted to enter a URL to scan
URL_TO_SCAN = str(input("URL: "))

# The URL is scanned using the VirusTotal API client
# The scan_url method sends the URL to VirusTotal for analysis
url_scan = client_vt.scan_url(URL_TO_SCAN)

# The scan_url method returns a URL object that contains information about the scan
# The URL object contains various attributes, including the scan ID and the analysis results
URL_ID = vt.url_id(URL_TO_SCAN)

# The scan ID is used to retrieve the analysis results from VirusTotal
# The get_object method retrieves the analysis results for the specified URL ID
# The URL ID is a unique identifier for the URL in VirusTotal's database
# The get_object method returns a URL object that contains the analysis results
# The URL object contains various attributes, including the last analysis results and the total votes
# The last analysis results contain the results from various antivirus vendors
# The total votes contain the number of votes from the community for the URL
# The last analysis results and total votes are used to determine the safety of the URL
# The last analysis results contain the results from various antivirus vendors
url_report = client_vt.get_object(f"/urls/{URL_ID}")

# Calculate the number of malicious and harmless results from corporate antivirus vendors
# The last_analysis_results attribute contains the results from various antivirus vendors
# Each vendor's result contains a category that indicates whether the URL is malicious or harmless
# The category is used to count the number of malicious and harmless results from corporate antivirus vendors
malicious_count = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'malicious')
harmless_count = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'harmless')


# Print the results in a table format using the tabulate library
# The tabulate library is used to create a table for displaying the results
# The table contains the results from corporate antivirus vendors and community votes
# The table is printed to the console using the print function
# The table is formatted using the "presto" table format
# The table contains the headers "Link Summary Result", "Malicious", and "Safe"
# The table contains the results from corporate antivirus vendors and community votes
# The table is printed to the console using the print function

# The Harmless is changed to Safe for better layman understanding
table = [
    ["Link Summary Result", "Malicious", "Safe"],
    ["Results", malicious_count, harmless_count]
]

print("\n") 
result = tabulate(table, headers="firstrow", tablefmt="presto")
print(result)

print("\n")

response = client_google.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"You are a cybersecurity expert. Based on the following data, If malicious > 1 = malicious. Please provide a short explanation of {result}, do not mention the rules."
)

print(response.text)

# close the VirusTotal client connection
# This is important to free up resources and avoid memory leaks    
client_vt.close()