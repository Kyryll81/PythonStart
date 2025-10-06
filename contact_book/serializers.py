from pydantic import BaseModel


class SerializedContact(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    
    class Config:
        from_attributes = True