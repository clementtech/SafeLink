import vt
import os
import sys
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()
try:
    API_KEY = os.getenv("API_KEY")
    client = vt.Client(API_KEY)

except ValueError:
    sys.exit("Please setup your API key in the .env file.")

except ModuleNotFoundError:
    sys.exit("Please install the required modules using 'pip install -r requirements.txt'.")
    
URL_TO_SCAN = str(input("URL: "))

url_scan = client.scan_url(URL_TO_SCAN)

URL_ID = vt.url_id(URL_TO_SCAN)
url_report = client.get_object(f"/urls/{URL_ID}")

malicious_count_corporate = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'malicious')
harmless_count_corporate = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'harmless')

community_score = url_report.total_votes
harmless_count_community = community_score["harmless"]
malicious_count_community = community_score["malicious"]

table = [
    ["Link Summary Result", "Malicious", "Safe"],
    ["Corporate AV Results", malicious_count_corporate, harmless_count_corporate],
    ["Community Votes", malicious_count_community, harmless_count_community]
]

print("\n") 
print(tabulate(table, headers="firstrow", tablefmt="presto"))
print("\n")

if malicious_count_corporate > 0:
    print("This URL is flagged as malicious! Please do not proceed unless you are sure it is safe.")

elif malicious_count_corporate == 0 and harmless_count_corporate > 0:
    print("This URL is considered safe by our partners, however please proceed with caution.")

print("\n")

if malicious_count_community > harmless_count_community:
    print("The community considers this URL is dangerous! Please do not proceed unless you are sure it is safe.")
    print("However, please note that the community votes are not always accurate.")

elif malicious_count_community == 0 and harmless_count_community == 0:
    print("This URL has no community votes. It might be new or not widely known.")
    print("Scammers often use new URLs to avoid detection.")
    
client.close()