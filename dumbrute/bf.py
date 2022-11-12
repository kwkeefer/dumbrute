from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable
from dataclasses import dataclass


@dataclass
class Creds:
    username: str
    password: str


def read_file(path: str) -> list:
    """Reads a file, returns a list of lines from the file"""
    with open(path) as f:
        return f.read().splitlines()


def user_pass_generator(usernames: Iterable, passwords: Iterable):
    """ Builds an interable of Creds objects, used by the brute force function """
    for username in usernames:
        for password in passwords:
            yield Creds(username, password)


def start_brute_force(function: Callable, usernames: Iterable, passwords: Iterable, threads: int = 5):
    """ Takes a function, a list of usernames and passwords, and the number of threads.
    Uses this info to start a brute force """
    creds = user_pass_generator(usernames=usernames, passwords=passwords)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(function, creds)

        for result in results:
            print(result)
