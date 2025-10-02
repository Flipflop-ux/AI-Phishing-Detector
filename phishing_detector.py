import re

def is_phishing(url):
    # Simple heuristic: suspicious keywords or unusual patterns
    suspicious_keywords = ["login", "secure", "bank", "update", "verify"]
    if any(word in url.lower() for word in suspicious_keywords):
        return True
    if re.search(r"\d{4,}", url):  # URLs with long numbers
        return True
    if "@" in url:  # @ symbol in URL often suspicious
        return True
    return False

# Example URLs
urls = [
    "http://secure-bank-login.com",
    "http://example.com/home",
    "http://update-account123.com"
]

for url in urls:
    result = "Phishing?" if is_phishing(url) else "Safe"
    print(f"{url} -> {result}")
