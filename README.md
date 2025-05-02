# SafeLink
SafeLink is a Python program that helps consumers and corporations by examining the safety of links to prevent phishing, with the help of the VirusTotal API.

### This Project now integrates with Google Gemini AI!
![gemini](https://s.yimg.com/ny/api/res/1.2/CKSDxCR76Wlcg35wWO_61A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MA--/https://s.yimg.com/os/creatr-uploaded-images/2023-12/5f7be670-943f-11ee-af7f-41b7060d20ba)

### Sneak Peek:
#### When Safe URL is provided:
![Screenshot](https://raw.githubusercontent.com/clementtech/SafeLink/refs/heads/main/assets/safe_link_result.png)

#### When Malicious URL is provided:
![Screenshot](https://raw.githubusercontent.com/clementtech/SafeLink/refs/heads/main/assets/malicious_link_result.png)

## Prerequisites:
- [Python](https://www.python.org/downloads/)
- [VirusTotal API Key](https://docs.virustotal.com/docs/please-give-me-an-api-key)
- [Google Gemini API Key](https://ai.google.dev/gemini-api/docs)

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
      API_KEY_VT = "Your VirusTotal API Key"
      API_KEY_Google = "Your Google Gemini API Key"
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

# Future Improvements:
- ~~Integration with Artificial Intelligence to provide better detection of phishing links~~
- Chrome extension to provide real-time detection of phishing links
- Android and iOS app to provide real-time detection of phishing links