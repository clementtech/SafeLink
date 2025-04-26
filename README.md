# SafeLink
SafeLink is a Python Program that helps consumers/coorporate by examine the safetyness of the link to prevent phishing with the help of VirusTotal API.

### Sneak Peek:
#### When Safe URL is provided:
![Screenshot](https://raw.githubusercontent.com/clementtech/SafeLink/refs/heads/main/assets/safe_link_result.png)

#### When Malicious URL is provided:
![Screenshot](https://raw.githubusercontent.com/clementtech/SafeLink/refs/heads/main/assets/malicious_link_result.png)

## Prerequisites:
- [Python](https://www.python.org/downloads/)
- [VirusTotal API Key](https://docs.virustotal.com/docs/please-give-me-an-api-key)

## How to use?
1. Download the project onto your computer
    - You can download the project with git by entering the command:
    ```
    git clone https://github.com/clementtech/SafeLink.git
    ```

2. Create an empty file with the name ".env" to store the VirusTotal API key
    - You can create the empty file in the same directory by using the following command:
    ```
    code .env
    ```
    - After creating the file, please enter your API key inside the ".env" file.
      Example:
      ```
      API_KEY = "Your API Key"
      ```

3. Download the required dependencies 
    - The dependencies can be installed by entering the following command:
    ```
    pip install -r requirements.txt
    ```

4. Done setup!
    - You can run the program by entering the following command:
    ```
    python main.py
    ```
