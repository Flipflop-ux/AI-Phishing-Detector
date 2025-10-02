
# AI Phishing Detector 🚨

A beginner-friendly cybersecurity project that detects potential phishing URLs using Python.  
Runs fully in GitHub — no local setup required — and uses **GitHub Actions** to execute automatically on push or manually via a button.

---

## 🔹 Features
- ✅ Detects suspicious URLs using keyword & pattern heuristics  
- ⚡ Automated with **GitHub Actions** (runs on push)  
- 🎛 Manual "Run workflow" button for on-demand testing  
- 🌐 Easy to test: edit URLs in the script or workflow input

---

## 🔹 Example Code
```python
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

