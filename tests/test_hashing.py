import pytest

from hash_service.hashing import make_hash, verify_hash

ABC_SHA256 = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def test_sha256_known_value():
    assert make_hash("abc") == ABC_SHA256


@pytest.mark.parametrize("algorithm, length", [
    ("md5", 32),
    ("sha1", 40),
    ("sha256", 64),
    ("sha512", 128),
])
def test_hash_length(algorithm, length):
    assert len(make_hash("test", algorithm)) == length


def test_unknown_algorithm():
    with pytest.raises(ValueError):
        make_hash("abc", "sha3")


def test_verify_correct_hash():
    assert verify_hash("abc", ABC_SHA256)


def test_verify_uppercase_hash():
    assert verify_hash("abc", ABC_SHA256.upper())


def test_verify_wrong_hash():
    assert not verify_hash("abd", ABC_SHA256)
