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
    # secure implementation: verify=True (or specifying a path to a trusted CA bundle)
    # enforces strict TLS certificate verification
    response = requests.get("https://localhost:8443/", verify="cert.pem")
    return response.json()


def invalid_example():
        response = requests.get("https://localhost:8443/", verify=True)
        return response.json()

def main ():
    print("Insecure output: ", insecure_example()) # output: {'status': 'success'} (Succeeds because validation is disabled)
    print("Secure output: ", fixed_example()) # output {'status': 'success} (Succeeds because validation is explicitly allowed)

    # output <error> (Fails because verify=True uses pythons default trusted certificate store not the one we created)
    try:
        print("Invalid output: ", invalid_example())
    except requests.exceptions.SSLError as e:
        print("Invalid example correctly rejected the certificate:", e)

# init
main()