import requests
import socket

# Define the target domain and the wordlist of subdomains to try
target_domain = "example.com"
subdomains = ["www", "mail", "ftp", "admin"]

# Loop through the list of subdomains and attempt to resolve the domain name
for subdomain in subdomains:
    try:
        # Construct the full domain name
        domain = f"{subdomain}.{target_domain}"

        # Resolve the IP address of the domain name
        ip_address = socket.gethostbyname(domain)

        # Print the IP address if it was found
        print(f"{domain}: {ip_address}")

    except socket.gaierror:
        # Ignore domain names that could not be resolved
        pass

