import hashlib
import hmac
import sys

USERS = {
    "student": "42e55121810b5867d70499dee4ba4aba9845b1574535ebaa9d96275c39225092",
}


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login(username, password):
    stored = USERS.get(username)
    if stored is None:
        return False
    return hmac.compare_digest(stored, hash_password(password))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python login.py <username> <password>")
        sys.exit(2)
    if login(sys.argv[1], sys.argv[2]):
        print("Access granted")
    else:
        print("Invalid username or password")
        sys.exit(1)
