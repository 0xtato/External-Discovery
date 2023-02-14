import argparse
import requests

def get_subdomains(domain):
    subdomains = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            subdomain = entry["name_value"].strip().lower()
            if not subdomain.startswith("*") and not subdomain.startswith("www."):
                subdomains.add(subdomain)
    return list(subdomains)

parser = argparse.ArgumentParser()
parser.add_argument("domain", help="the domain to gather subdomains for")
parser.add_argument("-o", "--output", help="the file to write the subdomains to")
args = parser.parse_args()

domain = args.domain
subdomains = get_subdomains(domain)

if args.output:
    with open(args.output, "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")
else:
    print("Subdomains:")
    print("\n".join(subdomains))
