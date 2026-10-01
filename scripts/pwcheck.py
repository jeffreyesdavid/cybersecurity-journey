import hashlib
import getpass
import requests

def check_password(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=10)
    response.raise_for_status()
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)
    return 0

password = getpass.getpass("Password to check: ")
count = check_password(password)

if count:
    print(f"Found {count:,} times in breaches. Change it.")
else:
    print("Not found in known breaches.")
