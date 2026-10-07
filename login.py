import hashlib
import hmac
import sys

ITERATIONS = 200_000
USERS = {
    "student": (
        "631390153b37efe0ee91c0db883ec77a",
        "7450d9284848ff40b0e52cb1761da77cfcb37645f630a341b175b3924588ae5c",
    ),
}


def hash_password(password, salt):
    data = password.encode("utf-8")
    key = hashlib.pbkdf2_hmac("sha256", data, bytes.fromhex(salt), ITERATIONS)
    return key.hex()


def login(username, password):
    if username not in USERS:
        return False
    salt, stored = USERS[username]
    return hmac.compare_digest(stored, hash_password(password, salt))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python login.py <username> <password>")
        sys.exit(2)
    if login(sys.argv[1], sys.argv[2]):
        print("Access granted")
    else:
        print("Invalid username or password")
        sys.exit(1)
