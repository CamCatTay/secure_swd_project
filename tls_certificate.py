# Vulnerability: Disabled TLS Certificate Verification
# Reference IDs: CWE-295 | OWASP Top 10:2021 A02 Cryptographic Failures
# Author: Cameron Taylor (M-4)

import requests
# suppress urllib3 InsecureRequestWarning for clean test output
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Insecure Code Snippet
def insecure_example():
    # vulnerable implementation: verify=False disables TLS certificate verification
    # leaving traffic vulnerable to MITM attacks
    response = requests.get("https://localhost:8443/", verify=False)
    return response.json()


# Fixed Code Snippet
def fixed_example():
    # secure implementation: verify=True (or specifying a path to a trusted CA bundle <-- contains root and intermediate certificates)
    # enforces strict TLS certificate verification
    response = requests.get("https://localhost:8443/", verify="cert.pem")
    return response.json()

print(insecure_example) # output: {'status': 'success'} (Succeeds because validation is disabled)
#print(fixed_example) # output {'status': 'success} (Succeeds because validation is explicitly allowed)