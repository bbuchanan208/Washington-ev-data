from pydantic import BaseModel


class EV_API_Data(BaseModel):
    make: str
    electric_range: int

class EV_Make_Metadata(BaseModel):
    make: str
    count: int
    average_range: float
