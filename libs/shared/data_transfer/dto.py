from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
    email: str

class ApiKeyCreateDTO(BaseModel):
    user_id: str
    is_admin: bool = False