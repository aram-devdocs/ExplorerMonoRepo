from libs.server.data_access import db, User
from libs.shared.data_transfer import UserCreateDTO

class UserService:
    @staticmethod
    def create_user(data: UserCreateDTO, user_id: str) -> User:
        user = User(name=data.name, email=data.email)
        user.track(user_id)
        db.session.add(user)
        db.session.commit()
        return user