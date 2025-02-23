import socket
import whois
import requests

def get_whois_info(domain):
    """Fetch WHOIS information for a domain."""
    try:
        w = whois.whois(domain)
        print(w)  # Print all WHOIS data to check what is available
        
        print("\n[WHOIS INFO]")
        print(f"Domain: {w.domain_name if w.domain_name else 'Not Available'}")
        print(f"Registrar: {w.registrar if w.registrar else 'Not Available'}")
        print(f"Expiration Date: {w.expiration_date if w.expiration_date else 'Not Available'}")
        print(f"Creation Date: {w.creation_date if w.creation_date else 'Not Available'}")
    except Exception as e:
        print(f"Error fetching WHOIS: {e}")

def get_ip_info(domain):
    """Find the IP address of a given domain."""
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[IP INFO] IP Address: {ip}")
        return ip
    except Exception as e:
        print(f"Error fetching IP: {e}")
        return None

def get_geolocation(ip):
    """Get geolocation details of an IP address."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(f"\n[GEOLOCATION] Country: {data.get('country')}, City: {data.get('city')}")
    except Exception as e:
        print(f"Error fetching geolocation: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain (e.g., google.com): ")
    get_whois_info(domain)
    ip = get_ip_info(domain)
    if ip:
        get_geolocation(ip)
