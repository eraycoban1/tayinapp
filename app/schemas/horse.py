from pydantic import BaseModel

class HorseCreate(BaseModel):
    name: str
    age: int
    breed: str

class HorseResponse(HorseCreate):
    id: int

    class Config:
        from_attributes = True
