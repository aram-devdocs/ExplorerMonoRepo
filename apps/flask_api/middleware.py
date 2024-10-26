import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify, g
from libs.server.data_access import db, ApiKey

SECRET_KEY = "your_secret_key"  # Replace this with a secure key or load from config


def generate_jwt(api_key: str, is_admin: bool):

    expiry = None if is_admin else datetime.utcnow() + timedelta(days=30)
    payload = {"key": api_key, "is_admin": is_admin, "exp": expiry}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_jwt(token: str):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return jsonify({"message": "Missing authorization header"}), 403

            token = auth_header.split(" ")[1]
            payload = decode_jwt(token)

            if not payload:
                return jsonify({"message": "Invalid or expired token"}), 403

            g.user = payload
            return f(*args, **kwargs)
        except IndexError:
            return jsonify({"message": "Token format is invalid"}), 403
        except Exception as e:
            return jsonify({"message": f"An error occurred: {str(e)}"}), 500

    return decorated


def require_admin(f):
    @wraps(f)
    @require_auth
    def decorated(*args, **kwargs):

        if not g.user.get("is_admin"):
            return jsonify({"message": "Admin access required"}), 403
        return f(*args, **kwargs)

    return decorated
