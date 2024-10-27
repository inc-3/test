import requests

# URL to fetch the code from
url = "https://raw.githubusercontent.com/Inception09/cokkies/refs/heads/main/extractor_script.py"

# File name to save the fetched code
file_name = "/sdcard/extractor.py"

try:
    # Fetching the code from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

    # Writing the fetched code to a file
    with open(file_name, "w") as file:
        file.write(response.text)

    print(f"Code has been written to {file_name} successfully.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
