import os
import sys

try:

    import vt
    from dotenv import load_dotenv
    from tabulate import tabulate
    from google import genai

    load_dotenv()

    API_KEY_VT = os.getenv("API_KEY_VT")
    API_KEY_Google = os.getenv("API_KEY_Google")
    client_vt = vt.Client(API_KEY_VT)
    client_google = genai.Client(api_key = API_KEY_Google)

except ValueError:
    sys.exit("Please setup your API key in the .env file.")

except ModuleNotFoundError:
    sys.exit("Please install the required modules using 'pip install -r requirements.txt'.")

URL_TO_SCAN = str(input("URL: "))

url_scan = client_vt.scan_url(URL_TO_SCAN)

URL_ID = vt.url_id(URL_TO_SCAN)

url_report = client_vt.get_object(f"/urls/{URL_ID}")

malicious_count = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'malicious')
harmless_count = sum(1 for vendor in url_report.last_analysis_results.values() if vendor['category'] == 'harmless')

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
 
client_vt.close()