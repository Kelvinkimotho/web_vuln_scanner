import requests

def test_sql_injection(target):
    payloads = ["' OR '1'='1", "' OR 'a'='a", "' OR 1=1--"]
    results = {}

    for payload in payloads:
        url = f"{target}/?id={payload}"
        try:
            response = requests.get(url)
            if "SQL" in response.text or "syntax" in response.text:
                results[payload] = "Vulnerable"
            else:
                results[payload] = "Safe"
        except requests.exceptions.RequestException:
            results[payload] = "Failed to check"

    return results
