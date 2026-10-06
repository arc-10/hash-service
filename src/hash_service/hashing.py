import hashlib
import hmac

ALGORITHMS = ("md5", "sha1", "sha256", "sha512")


def make_hash(text, algorithm="sha256"):
    if algorithm not in ALGORITHMS:
        raise ValueError(f"unsupported algorithm: {algorithm}")
    return hashlib.new(algorithm, text.encode("utf-8")).hexdigest()


def verify_hash(text, expected, algorithm="sha256"):
    return hmac.compare_digest(make_hash(text, algorithm), expected.lower())
