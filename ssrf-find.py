import requests
from bs4 import BeautifulSoup

# Define the target URL
target_url = 'http://example.com'

# Send a GET request to the target URL
response = requests.get(target_url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all form elements
forms = soup.find_all('form')

# Extract input parameters from forms
for form in forms:
    inputs = form.find_all('input')
    for input in inputs:
        # Check if the input type is 'url' or similar
        if 'url' in input.get('type', ''):
            parameter_name = input.get('name', '')
            print('Potential SSRF parameter:', parameter_name)

# Find other potential SSRF parameters in URLs and headers
for tag in soup.find_all():
    # Check if URL attributes contain potential SSRF parameters
    for attribute in ['href', 'src']:
        attribute_value = tag.get(attribute, '')
        if 'http://' in attribute_value or 'https://' in attribute_value:
            if 'localhost' not in attribute_value and '127.0.0.1' not in attribute_value:
                print('Potential SSRF parameter in', attribute, ':', attribute_value)

    # Check if headers contain potential SSRF parameters
    for attribute in ['X-Forwarded-For', 'Referer']:
        header_value = tag.get('headers', {}).get(attribute, '')
        if 'http://' in header_value or 'https://' in header_value:
            if 'localhost' not in header_value and '127.0.0.1' not in header_value:
                print('Potential SSRF parameter in header', attribute, ':', header_value)


