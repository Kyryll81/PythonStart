from pydantic import BaseModel


class SerializedRecord(BaseModel):
    id: int
    subject: str
    teacher: str
    grade: int
    date: str  # too many problems with parse
    
    class Config:
        from_attributes = True
