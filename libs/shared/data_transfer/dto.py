from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
    email: str