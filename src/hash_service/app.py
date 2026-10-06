from flask import Flask, jsonify, request

from hash_service.hashing import ALGORITHMS, make_hash, verify_hash

app = Flask(__name__)


def read_request(*fields):
    data = request.get_json(silent=True) or {}
    algorithm = data.get("algorithm", "sha256")
    if any(not isinstance(data.get(f), str) for f in fields):
        return None, "required fields: " + ", ".join(fields)
    if algorithm not in ALGORITHMS:
        return None, f"unsupported algorithm: {algorithm}"
    return data | {"algorithm": algorithm}, None


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/hash")
def hash_text():
    data, error = read_request("text")
    if error:
        return jsonify(error=error), 400
    return jsonify(algorithm=data["algorithm"], hash=make_hash(data["text"], data["algorithm"]))


@app.post("/verify")
def verify():
    data, error = read_request("text", "hash")
    if error:
        return jsonify(error=error), 400
    return jsonify(match=verify_hash(data["text"], data["hash"], data["algorithm"]))
