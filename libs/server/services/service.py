import uuid
from libs.server.data_access import db, User, ApiKey
from libs.shared.data_transfer import UserCreateDTO, ApiKeyCreateDTO
import hashlib
import os
from cryptography.fernet import Fernet


class UserService:
    @staticmethod
    def create_user(data: UserCreateDTO, requester_user_id: str) -> User:
        try:
            user = User(name=data.name, email=data.email)
            user.track(requester_user_id)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e


class ApiKeyService:
    @staticmethod
    def create_api_key(data: ApiKeyCreateDTO, requester_user_id: str) -> ApiKey:
        try:
            # Generate a new API key
            raw_api_key = str(uuid.uuid4())

            # Salt and hash the API key
            salt = os.urandom(16)
            salted_key = salt + raw_api_key.encode()
            hashed_key = hashlib.sha256(salted_key).digest()

            # Encrypt the hashed key
            encryption_key = Fernet.generate_key()
            fernet = Fernet(encryption_key)
            encrypted_key = fernet.encrypt(hashed_key)

            # Store the encrypted key and salt in the database
            api_key = ApiKey(
                id=str(uuid.uuid4()),
                key=encrypted_key,
                is_admin=data['is_admin'],
                user_id=data['user_id'],
            )
            api_key.track(requester_user_id)
            db.session.add(api_key)
            db.session.commit()

            # Return the raw API key to the user
            return api_key
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def read_api_key(api_key_id: str) -> str:
        try:
            api_key = db.session.query(ApiKey).filter_by(id=api_key_id).first()
            if not api_key:
                raise ValueError("API key not found")

            # Decrypt the stored key
            fernet = Fernet(api_key.encryption_key)
            decrypted_key = fernet.decrypt(api_key.key)

            # Return the decrypted key
            return decrypted_key.decode()
        except Exception as e:
            raise e
