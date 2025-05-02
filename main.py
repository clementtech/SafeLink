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
malicious_count_corporate = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'malicious')
harmless_count_corporate = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'harmless')

# Calculate the number of malicious and harmless results from the community
# The total_votes attribute contains the number of votes from the community for the URL
# The total_votes attribute contains two keys: "harmless" and "malicious"
# The values of these keys are used to count the number of malicious and harmless results from the community
# The total_votes attribute is used to determine the safety of the URL based on community votes
# The total_votes attribute contains the number of votes from the community for the URL
community_score = url_report.total_votes
harmless_count_community = community_score["harmless"]
malicious_count_community = community_score["malicious"]

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
    ["Corporate AV Results", malicious_count_corporate, harmless_count_corporate],
    ["Community Votes", malicious_count_community, harmless_count_community]
]

print("\n") 
print(tabulate(table, headers="firstrow", tablefmt="presto"))
print("\n")

# If the number of malicious results from corporate antivirus vendors is greater than 0, the URL is considered malicious
# Of course, false positives can happen, so the user is advised to proceed with caution
if malicious_count_corporate > 0:
    print("This URL is flagged as malicious! Please do not proceed unless you are sure it is safe.")

# If the number of malicious results from corporate antivirus vendors is 0 and the number of harmless results is greater than 0, the URL is considered safe
# However, the user is advised to proceed with caution as false negatives can happen
elif malicious_count_corporate == 0 and harmless_count_corporate > 0:
    print("This URL is considered safe by our partners, however please proceed with caution.")

print("\n")

# If the number of malicious results from the community is greater than the number of harmless results, the URL is considered dangerous
# However, community votes are not always accurate, so the user is advised to proceed with caution
if malicious_count_community > harmless_count_community:
    print("The community considers this URL is dangerous! Please do not proceed unless you are sure it is safe.")
    print("However, please note that the community votes are not always accurate.")

# If the URL does not have any community votes, the user is advised to proceed with caution
# As the URL might be new or not widely known, scammers often use new URLs to avoid detection
elif malicious_count_community == 0 and harmless_count_community == 0:
    print("This URL has no community votes. It might be new or not widely known.")
    print("Scammers often use new URLs to avoid detection.")

# close the VirusTotal client connection
# This is important to free up resources and avoid memory leaks    
client_vt.close()

# response = client_google.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)
