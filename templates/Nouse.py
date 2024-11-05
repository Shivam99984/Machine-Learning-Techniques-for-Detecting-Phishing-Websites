import requests
import base64

# Replace with your VirusTotal API key
API_KEY = '3768d06d65d69d0c543d482a460cf4664178a0211f1bb24b20e2b8f440a43ec9'

# Function to encode the URL to base64 format (as required by VirusTotal API v3)
def url_to_base64(url):
    # Strip 'http://' or 'https://' from the URL before encoding
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return encoded_url

# Function to submit the URL for analysis
def submit_url_for_analysis(url):
    submit_url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": API_KEY
    }
    data = {"url": url}

    response = requests.post(submit_url, headers=headers, data=data)
    
    if response.status_code == 200:
        json_response = response.json()
        # Extract the URL ID for further analysis
        url_id = json_response['data']['id']
        return url_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get the URL analysis report
def get_url_report(url_id):
    report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(report_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Main function
def analyze_website(url):
    # Step 1: Submit the URL for analysis
    url_id = submit_url_for_analysis(url)
    if not url_id:
        print("Failed to submit the URL.")
        return

    # Step 2: Get the URL analysis report using the base64 encoded ID
    encoded_url_id = url_to_base64(url)
    report = get_url_report(encoded_url_id)

    if report:
        # Step 3: Parse the report
        phishing_status = report['data']['attributes']['last_analysis_stats']['malicious']
        categories = report['data']['attributes'].get('categories', {})

        # Display results
        print(f"Phishing Status: {'Yes' if phishing_status > 0 else 'No'}")
        print(f"Content Categories: {', '.join(categories.values()) if categories else 'Unknown'}")
    else:
        print("Failed to retrieve the report.")

# Example usage:
if __name__ == "__main__":
    url_to_analyze = input("Enter the URL to analyze: ")
    analyze_website(url_to_analyze)
