# WHOIS & IP Lookup Tool

This is a simple Python script that retrieves WHOIS information, IP addresses, and geolocation details for a given domain.

## Features
- Fetches WHOIS information (domain owner, registrar, expiry date, creation date).
- Finds the IP address of a domain.
- Retrieves geolocation details of the IP (country, city).

## Installation
Ensure you have Python installed, then install the required dependencies:
```sh
pip install python-whois requests
```

## Usage
Run the script and enter a domain when prompted:
```sh
python whois_lookup.py
```
Example input:
```
Enter a domain (e.g., google.com): google.com
```

## Output Example
```
[WHOIS INFO]
Domain: google.com
Registrar: MarkMonitor Inc.
Expiration Date: 2029-09-14
Creation Date: 1997-09-15

[IP INFO] IP Address: 142.250.190.14

[GEOLOCATION] Country: US, City: Mountain View
```

## Notes
- Some domains may have restricted WHOIS information.
- Ensure you have an active internet connection for IP geolocation.

## License
This project is free to use and modify.

