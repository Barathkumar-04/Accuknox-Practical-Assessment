import requests

def check_application_status(url):
    try:
        # Send an HTTP GET request to the application
        response = requests.get(url)
        
        # Check the HTTP status code
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred while checking the application: {e}")

# Example usage
if __name__ == "__main__":
    app_url = "http://example.com"  # Replace with your application's URL
    check_application_status(app_url)