import re

def is_phishing(url):
    suspicious_keywords = ["login", "secure", "bank", "update", "verify"]
    if any(word in url.lower() for word in suspicious_keywords):
        return True
    if re.search(r"\d{4,}", url):
        return True
    if "@" in url:
        return True
    return False

# Example URLs
urls = [
    "http://secure-bank-login.com",
    "http://example.com/home",
    "http://update-account123.com",
    "http://safe-site.org"
]

for url in urls:
    if is_phishing(url):
        print(f"🚨 {url} -> Likely PHISHING")
    else:
        print(f"✅ {url} -> Safe")
